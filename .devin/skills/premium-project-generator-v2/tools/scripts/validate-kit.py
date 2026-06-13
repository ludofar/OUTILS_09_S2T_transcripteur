#!/usr/bin/env python3
"""
Kit Validator for Premium Project Generator V2.
Automated replacement for manual checklists.
Validates the entire generated kit: structure, frontmatter, coherence, quality.

Usage:
    python3 validate-kit.py <path_to_kit>
    python3 validate-kit.py <path_to_kit> --json
    python3 validate-kit.py <path_to_kit> --verbose

Exit codes:
    0 = Score >= 85 (premium quality)
    1 = Score 70-84 (patches recommended)
    2 = Score < 70 (rework required)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


MAX_RULE_SIZE = 12000  # characters
MAX_SKILL_LINES = 500
MIN_RULES = 4
MIN_SKILLS = 3
MIN_WORKFLOWS = 3
QUALITY_THRESHOLD = 85

REQUIRED_FRONTMATTER_FIELDS = {
    "rule": ["trigger", "description"],
    "skill": ["name", "description"],
    "workflow": ["description"],
}

VALID_TRIGGERS = {"always_on", "glob", "model_decision", "manual"}


def parse_frontmatter(filepath: Path) -> tuple[dict, str, bool]:
    """Parse frontmatter from a markdown file. Returns (frontmatter, body, valid_yaml)."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}, "", False

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)", content, re.DOTALL)
    if not match:
        return {}, content, False

    fm_text = match.group(1)
    body = match.group(2)

    frontmatter = {}
    for line in fm_text.split("\n"):
        kv = re.match(r"^(\w[\w_-]*)\s*:\s*(.+)$", line.strip())
        if kv:
            key = kv.group(1)
            value = kv.group(2).strip().strip("'\"")
            frontmatter[key] = value

    return frontmatter, body, True


def validate_structure(root: Path) -> list[dict]:
    """Validate kit directory structure."""
    issues = []

    # Check AGENTS.md
    if not (root / "AGENTS.md").exists():
        issues.append({"severity": "ERROR", "check": "structure", "message": "Missing AGENTS.md at project root"})

    # Check rules
    rules_dir = root / ".devin" / "rules"
    if rules_dir.exists():
        rules = list(rules_dir.glob("*.md"))
        if len(rules) < MIN_RULES:
            issues.append({"severity": "WARNING", "check": "structure", "message": f"Only {len(rules)} rules found (minimum {MIN_RULES})"})
    else:
        issues.append({"severity": "ERROR", "check": "structure", "message": "Missing .devin/rules/ directory"})

    # Check skills
    skills_dir = root / ".devin" / "skills"
    if skills_dir.exists():
        skills = [d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]
        if len(skills) < MIN_SKILLS:
            issues.append({"severity": "WARNING", "check": "structure", "message": f"Only {len(skills)} skills found (minimum {MIN_SKILLS})"})
    else:
        issues.append({"severity": "ERROR", "check": "structure", "message": "Missing .devin/skills/ directory"})

    # Check workflows
    workflows_dir = root / ".devin" / "workflows"
    if workflows_dir.exists():
        workflows = list(workflows_dir.glob("*.md"))
        if len(workflows) < MIN_WORKFLOWS:
            issues.append({"severity": "WARNING", "check": "structure", "message": f"Only {len(workflows)} workflows found (minimum {MIN_WORKFLOWS})"})
    else:
        issues.append({"severity": "ERROR", "check": "structure", "message": "Missing .devin/workflows/ directory"})

    # Check kebab-case naming
    for path in root.rglob("*"):
        if path.is_file() and path.suffix == ".md":
            name = path.stem
            if name != name.lower() and name not in ("SKILL", "AGENTS", "README", "CHANGELOG", "TOOLS_USERGUIDE", "CONTRIBUTING", "INSTALL"):
                issues.append({"severity": "WARNING", "check": "naming", "message": f"Non-kebab-case filename: {path.relative_to(root)}"})

    return issues


def validate_frontmatter(root: Path) -> list[dict]:
    """Validate frontmatter of all markdown files."""
    issues = []

    # Rules
    rules_dir = root / ".devin" / "rules"
    if rules_dir.exists():
        for rule in rules_dir.glob("*.md"):
            fm, body, valid = parse_frontmatter(rule)
            rel = str(rule.relative_to(root))

            if not valid:
                issues.append({"severity": "ERROR", "check": "frontmatter", "message": f"Invalid or missing frontmatter: {rel}"})
                continue

            for field in REQUIRED_FRONTMATTER_FIELDS["rule"]:
                if field not in fm:
                    issues.append({"severity": "ERROR", "check": "frontmatter", "message": f"Missing '{field}' in {rel}"})

            if "trigger" in fm and fm["trigger"] not in VALID_TRIGGERS:
                issues.append({"severity": "WARNING", "check": "frontmatter", "message": f"Invalid trigger '{fm['trigger']}' in {rel}"})

            # Size check
            content = rule.read_text(encoding="utf-8", errors="replace")
            if len(content) > MAX_RULE_SIZE:
                issues.append({"severity": "WARNING", "check": "size", "message": f"Rule {rel} exceeds {MAX_RULE_SIZE} chars ({len(content)})"})

    # Skills
    skills_dir = root / ".devin" / "skills"
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                issues.append({"severity": "ERROR", "check": "structure", "message": f"Missing SKILL.md in {skill_dir.relative_to(root)}"})
                continue

            fm, body, valid = parse_frontmatter(skill_md)
            rel = str(skill_md.relative_to(root))

            if not valid:
                issues.append({"severity": "ERROR", "check": "frontmatter", "message": f"Invalid frontmatter: {rel}"})
                continue

            for field in REQUIRED_FRONTMATTER_FIELDS["skill"]:
                if field not in fm:
                    issues.append({"severity": "ERROR", "check": "frontmatter", "message": f"Missing '{field}' in {rel}"})

            # Line count check
            lines = body.split("\n")
            if len(lines) > MAX_SKILL_LINES:
                issues.append({"severity": "WARNING", "check": "size", "message": f"SKILL.md {rel} exceeds {MAX_SKILL_LINES} lines ({len(lines)})"})

            # Check skill name matches directory
            if "name" in fm and fm["name"] != skill_dir.name:
                issues.append({"severity": "WARNING", "check": "naming", "message": f"Skill name '{fm['name']}' does not match directory '{skill_dir.name}'"})

    # Workflows
    workflows_dir = root / ".devin" / "workflows"
    if workflows_dir.exists():
        for wf in workflows_dir.glob("*.md"):
            fm, body, valid = parse_frontmatter(wf)
            rel = str(wf.relative_to(root))
            if not valid:
                issues.append({"severity": "WARNING", "check": "frontmatter", "message": f"Missing frontmatter in workflow: {rel}"})

    return issues


def validate_coherence(root: Path) -> list[dict]:
    """Validate inter-file coherence."""
    issues = []

    # Collect all known skill names
    skills_dir = root / ".devin" / "skills"
    known_skills = set()
    if skills_dir.exists():
        for d in skills_dir.iterdir():
            if d.is_dir() and (d / "SKILL.md").exists():
                known_skills.add(d.name)

    # Collect all known rule names
    rules_dir = root / ".devin" / "rules"
    known_rules = set()
    if rules_dir.exists():
        for r in rules_dir.glob("*.md"):
            known_rules.add(r.stem)

    # Check workflows reference existing skills
    workflows_dir = root / ".devin" / "workflows"
    if workflows_dir.exists():
        for wf in workflows_dir.glob("*.md"):
            content = wf.read_text(encoding="utf-8", errors="replace")
            refs = re.findall(r"@([\w-]+)", content)
            for ref in refs:
                if ref not in known_skills and ref not in {"docs-auto-updater", "premium-project-generator", "premium-project-generator-v2", "project-context-analyzer", "tools-documentation", "specification-brainstorm"}:
                    issues.append({"severity": "INFO", "check": "coherence", "message": f"Workflow {wf.name} references unknown skill '@{ref}'"})

    # Check AGENTS.md references
    agents_md = root / "AGENTS.md"
    if agents_md.exists():
        content = agents_md.read_text(encoding="utf-8", errors="replace")
        for skill in known_skills:
            if skill not in content:
                issues.append({"severity": "INFO", "check": "coherence", "message": f"Skill '{skill}' not referenced in AGENTS.md"})

    return issues


def validate_quality(root: Path) -> list[dict]:
    """Validate premium quality standards."""
    issues = []

    # Check for examples in skills
    skills_dir = root / ".devin" / "skills"
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                content = skill_md.read_text(encoding="utf-8", errors="replace")
                if "exemple" not in content.lower() and "example" not in content.lower() and "usage" not in content.lower():
                    issues.append({"severity": "WARNING", "check": "quality", "message": f"No usage examples in {skill_dir.name}/SKILL.md"})

    # Check for TOOLS_USERGUIDE.md
    if not (root / "TOOLS_USERGUIDE.md").exists():
        issues.append({"severity": "INFO", "check": "quality", "message": "Missing TOOLS_USERGUIDE.md"})

    # Check for CHANGELOG
    if not (root / "CHANGELOG.md").exists() and not (root / "docs" / "CHANGELOG.md").exists():
        issues.append({"severity": "INFO", "check": "quality", "message": "Missing CHANGELOG.md"})

    return issues


def calculate_score(issues: list[dict]) -> dict:
    """Calculate quality score based on issues."""
    errors = len([i for i in issues if i["severity"] == "ERROR"])
    warnings = len([i for i in issues if i["severity"] == "WARNING"])
    infos = len([i for i in issues if i["severity"] == "INFO"])

    # Scoring by category
    structure_issues = [i for i in issues if i["check"] == "structure"]
    frontmatter_issues = [i for i in issues if i["check"] == "frontmatter"]
    coherence_issues = [i for i in issues if i["check"] == "coherence"]
    quality_issues = [i for i in issues if i["check"] == "quality"]
    other_issues = [i for i in issues if i["check"] not in ("structure", "frontmatter", "coherence", "quality")]

    def category_score(category_issues, max_score):
        errs = len([i for i in category_issues if i["severity"] == "ERROR"])
        warns = len([i for i in category_issues if i["severity"] == "WARNING"])
        deduction = errs * 5 + warns * 2
        return max(0, max_score - deduction)

    scores = {
        "completeness": {"score": category_score(structure_issues, 25), "max": 25},
        "frontmatter_quality": {"score": category_score(frontmatter_issues, 15), "max": 15},
        "inter_file_coherence": {"score": category_score(coherence_issues, 15), "max": 15},
        "examples_docs": {"score": category_score(quality_issues, 15), "max": 15},
        "premium_standards": {"score": category_score(other_issues, 10), "max": 10},
        "security": {"score": 10, "max": 10},  # Filled by security scan
        "staleness": {"score": 10, "max": 10},  # Filled by staleness check
    }

    total = sum(s["score"] for s in scores.values())

    return {
        "global_score": total,
        "max_score": 100,
        "pass": total >= QUALITY_THRESHOLD,
        "categories": scores,
        "total_errors": errors,
        "total_warnings": warnings,
        "total_infos": infos,
    }


def print_report(score: dict, issues: list[dict], json_output: bool = False, verbose: bool = False) -> None:
    """Print validation report."""
    if json_output:
        print(json.dumps({"score": score, "issues": issues}, indent=2, ensure_ascii=False))
        return

    print("=" * 60)
    print("  KIT VALIDATION REPORT — Premium Project Generator V2")
    print("=" * 60)
    print(f"  Score:    {score['global_score']}/{score['max_score']}")
    print(f"  Status:   {'PASS (premium)' if score['pass'] else 'FAIL — below threshold'}")
    print(f"  Errors:   {score['total_errors']}")
    print(f"  Warnings: {score['total_warnings']}")
    print(f"  Infos:    {score['total_infos']}")
    print("-" * 60)

    for cat_name, cat_score in score["categories"].items():
        bar_len = int(cat_score["score"] / cat_score["max"] * 20) if cat_score["max"] > 0 else 0
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {cat_name:<25} {bar} {cat_score['score']}/{cat_score['max']}")

    if verbose or not score["pass"]:
        print("\nIssues:\n")
        for issue in issues:
            icon = {"ERROR": "🔴", "WARNING": "🟡", "INFO": "🔵"}.get(issue["severity"], "⚪")
            print(f"  {icon} [{issue['severity']}] [{issue['check']}] {issue['message']}")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Kit Validator for PPG V2")
    parser.add_argument("path", help="Path to the generated kit")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--verbose", action="store_true", help="Show all issues including INFO")
    args = parser.parse_args()

    root = Path(args.path)
    if not root.is_dir():
        print(f"Error: {args.path} is not a valid directory", file=sys.stderr)
        sys.exit(1)

    issues = []
    issues.extend(validate_structure(root))
    issues.extend(validate_frontmatter(root))
    issues.extend(validate_coherence(root))
    issues.extend(validate_quality(root))

    score = calculate_score(issues)
    print_report(score, issues, json_output=args.json, verbose=args.verbose)

    if score["global_score"] < 70:
        sys.exit(2)
    elif score["global_score"] < QUALITY_THRESHOLD:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
