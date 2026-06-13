#!/usr/bin/env python3
"""
Cross-Platform Export for Premium Project Generator V2.
Exports Windsurf-generated tools (Rules, Skills, Workflows) to 14+ IDE platforms.

Supported platforms:
  Tier 1 (native SKILL.md): Claude Code, Copilot, Codex CLI, Gemini CLI, Kiro, Antigravity, Goose, OpenCode
  Tier 2 (auto-adapted):    Cursor (.mdc), Windsurf (.md), Cline, Roo Code, Trae
  Tier 3 (manual):          Zed, Junie, Aider

Usage:
    python3 cross-platform-export.py <path_to_kit>
    python3 cross-platform-export.py <path_to_kit> --platform cursor
    python3 cross-platform-export.py <path_to_kit> --platform all
    python3 cross-platform-export.py <path_to_kit> --json

Exit codes:
    0 = Export successful
    1 = Export failed
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional


PLATFORM_CONFIG = {
    "claude-code": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.claude/skills/",
        "project_path": ".claude/skills/",
        "description": "Claude Code (reads SKILL.md natively)",
    },
    "copilot": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.claude/skills/",
        "project_path": ".github/skills/",
        "description": "GitHub Copilot (shared path with Claude Code)",
    },
    "codex": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.agents/skills/",
        "project_path": ".agents/skills/",
        "description": "Codex CLI (universal agents path)",
    },
    "gemini": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.gemini/skills/",
        "project_path": None,
        "description": "Gemini CLI",
    },
    "kiro": {
        "tier": 1,
        "format": "skill.md",
        "global_path": None,
        "project_path": ".kiro/skills/",
        "description": "Kiro",
    },
    "antigravity": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.agents/skills/",
        "project_path": ".agents/skills/",
        "description": "Antigravity (universal agents path)",
    },
    "goose": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.config/goose/skills/",
        "project_path": None,
        "description": "Goose",
    },
    "opencode": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.config/opencode/skills/",
        "project_path": None,
        "description": "OpenCode",
    },
    "cursor": {
        "tier": 2,
        "format": "mdc",
        "global_path": None,
        "project_path": ".cursor/rules/",
        "description": "Cursor (auto-generates .mdc files)",
    },
    "windsurf": {
        "tier": 2,
        "format": "windsurf-md",
        "global_path": "~/.codeium/windsurf/",
        "project_path": ".devin/rules/",
        "description": "Windsurf (native .md rules)",
    },
    "cline": {
        "tier": 2,
        "format": "plain-md",
        "global_path": None,
        "project_path": ".clinerules/",
        "description": "Cline",
    },
    "roo-code": {
        "tier": 2,
        "format": "plain-md",
        "global_path": None,
        "project_path": ".roo/rules/",
        "description": "Roo Code",
    },
    "trae": {
        "tier": 2,
        "format": "plain-md",
        "global_path": None,
        "project_path": ".trae/rules/",
        "description": "Trae",
    },
    "universal": {
        "tier": 1,
        "format": "skill.md",
        "global_path": "~/.agents/skills/",
        "project_path": ".agents/skills/",
        "description": "Universal path (Codex, Gemini, Kiro, Antigravity)",
    },
}


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Split a markdown file into frontmatter dict and body."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)", content, re.DOTALL)
    if not match:
        return {}, content

    fm_text = match.group(1)
    body = match.group(2)

    frontmatter = {}
    for line in fm_text.split("\n"):
        kv = re.match(r"^(\w[\w_-]*)\s*:\s*(.+)$", line.strip())
        if kv:
            frontmatter[kv.group(1)] = kv.group(2).strip().strip("'\"")

    return frontmatter, body


def convert_to_mdc(filepath: Path, skill_name: str) -> str:
    """Convert a SKILL.md or Rule .md to Cursor .mdc format."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    frontmatter, body = parse_frontmatter(content)

    description = frontmatter.get("description", "")
    # Cursor .mdc format
    mdc_lines = [
        "---",
        f"description: {description}",
        "globs: ",
        "alwaysApply: false",
        "---",
        "",
        body.strip(),
    ]
    return "\n".join(mdc_lines)


def convert_to_plain_md(filepath: Path) -> str:
    """Convert a SKILL.md to plain markdown (strip frontmatter)."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    _, body = parse_frontmatter(content)
    return body.strip()


def convert_to_windsurf_rule(filepath: Path, skill_name: str) -> str:
    """Convert a SKILL.md to Windsurf rule .md format."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    frontmatter, body = parse_frontmatter(content)

    description = frontmatter.get("description", "")
    rule_lines = [
        "---",
        f"trigger: model_decision",
        f"description: {description}",
        "---",
        "",
        body.strip(),
    ]
    return "\n".join(rule_lines)


def find_exportable_files(root_path: str) -> list[dict]:
    """Find all exportable Windsurf tools in the kit."""
    root = Path(root_path)
    files = []

    # SKILL.md files
    for skill_md in root.rglob("SKILL.md"):
        rel = skill_md.relative_to(root)
        name = skill_md.parent.name if skill_md.parent != root else "main"
        files.append({
            "path": skill_md,
            "relative": str(rel),
            "type": "skill",
            "name": name,
        })

    # Rules
    rules_dir = root / ".devin" / "rules"
    if rules_dir.exists():
        for rule in rules_dir.glob("*.md"):
            files.append({
                "path": rule,
                "relative": str(rule.relative_to(root)),
                "type": "rule",
                "name": rule.stem,
            })

    # Workflows
    workflows_dir = root / ".devin" / "workflows"
    if workflows_dir.exists():
        for wf in workflows_dir.glob("*.md"):
            files.append({
                "path": wf,
                "relative": str(wf.relative_to(root)),
                "type": "workflow",
                "name": wf.stem,
            })

    # AGENTS.md
    agents_md = root / "AGENTS.md"
    if agents_md.exists():
        files.append({
            "path": agents_md,
            "relative": "AGENTS.md",
            "type": "agents",
            "name": "agents",
        })

    return files


def export_for_platform(
    root_path: str,
    platform: str,
    output_dir: str,
    files: list[dict],
) -> dict:
    """Export all tools for a specific platform."""
    config = PLATFORM_CONFIG[platform]
    out = Path(output_dir) / platform
    out.mkdir(parents=True, exist_ok=True)

    exported = []
    errors = []

    for file_info in files:
        filepath = file_info["path"]
        name = file_info["name"]

        try:
            if config["format"] == "skill.md":
                # Tier 1: copy as-is (SKILL.md native)
                if file_info["type"] == "skill":
                    dest_dir = out / name
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    # Copy entire skill directory
                    src_dir = filepath.parent
                    for item in src_dir.rglob("*"):
                        if item.is_file():
                            rel = item.relative_to(src_dir)
                            dest = dest_dir / rel
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(item, dest)
                    exported.append({"file": name, "format": "SKILL.md", "dest": str(dest_dir)})
                else:
                    dest = out / filepath.name
                    shutil.copy2(filepath, dest)
                    exported.append({"file": name, "format": "md", "dest": str(dest)})

            elif config["format"] == "mdc":
                # Tier 2 Cursor: convert to .mdc
                mdc_content = convert_to_mdc(filepath, name)
                dest = out / f"{name}.mdc"
                dest.write_text(mdc_content, encoding="utf-8")
                exported.append({"file": name, "format": ".mdc", "dest": str(dest)})

            elif config["format"] == "windsurf-md":
                # Tier 2 Windsurf: convert to rule .md
                if file_info["type"] == "skill":
                    rule_content = convert_to_windsurf_rule(filepath, name)
                    dest = out / f"{name}.md"
                    dest.write_text(rule_content, encoding="utf-8")
                    exported.append({"file": name, "format": "windsurf-rule", "dest": str(dest)})
                else:
                    dest = out / filepath.name
                    shutil.copy2(filepath, dest)
                    exported.append({"file": name, "format": "md", "dest": str(dest)})

            elif config["format"] == "plain-md":
                # Tier 2 Cline/Roo/Trae: strip frontmatter
                plain = convert_to_plain_md(filepath)
                dest = out / f"{name}.md"
                dest.write_text(plain, encoding="utf-8")
                exported.append({"file": name, "format": "plain-md", "dest": str(dest)})

        except Exception as e:
            errors.append({"file": name, "error": str(e)})

    # Generate install instructions
    install_instructions = _generate_install_instructions(platform, name, out)
    instructions_file = out / "INSTALL.md"
    instructions_file.write_text(install_instructions, encoding="utf-8")

    return {
        "platform": platform,
        "tier": config["tier"],
        "description": config["description"],
        "format": config["format"],
        "exported_files": len(exported),
        "errors": len(errors),
        "output_dir": str(out),
        "files": exported,
        "install_path": config.get("project_path") or config.get("global_path"),
    }


def _generate_install_instructions(platform: str, skill_name: str, export_dir: Path) -> str:
    """Generate platform-specific install instructions."""
    config = PLATFORM_CONFIG[platform]
    global_path = config.get("global_path", "")
    project_path = config.get("project_path", "")

    lines = [
        f"# Installation — {config['description']}",
        "",
        f"Platform: **{platform}** (Tier {config['tier']})",
        f"Format: `{config['format']}`",
        "",
        "## Install",
        "",
    ]

    if global_path:
        expanded = global_path.replace("~", "$HOME")
        lines.append(f"### Global install (all projects)")
        lines.append(f"```bash")
        lines.append(f"cp -R {export_dir}/* {global_path}{skill_name}/")
        lines.append(f"```")
        lines.append("")

    if project_path:
        lines.append(f"### Per-project install")
        lines.append(f"```bash")
        lines.append(f"cp -R {export_dir}/* {project_path}{skill_name}/")
        lines.append(f"```")
        lines.append("")

    return "\n".join(lines)


def generate_report(results: list[dict], root_path: str) -> dict:
    """Generate export report."""
    total_exported = sum(r["exported_files"] for r in results)
    total_errors = sum(r["errors"] for r in results)

    return {
        "export_date": datetime.now().isoformat(),
        "source_path": root_path,
        "platforms_exported": len(results),
        "total_files_exported": total_exported,
        "total_errors": total_errors,
        "results": results,
    }


def print_report(report: dict, json_output: bool = False) -> None:
    """Print the export report."""
    if json_output:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    print("=" * 60)
    print("  CROSS-PLATFORM EXPORT — Premium Project Generator V2")
    print("=" * 60)
    print(f"  Source:    {report['source_path']}")
    print(f"  Date:      {report['export_date']}")
    print(f"  Platforms: {report['platforms_exported']}")
    print(f"  Files:     {report['total_files_exported']}")
    print(f"  Errors:    {report['total_errors']}")
    print("-" * 60)

    for r in report["results"]:
        icon = "✅" if r["errors"] == 0 else "⚠️"
        print(f"  {icon} {r['platform']:<15} Tier {r['tier']}  {r['exported_files']} files  → {r['output_dir']}")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Cross-Platform Export for PPG V2")
    parser.add_argument("path", help="Path to the Windsurf kit to export")
    parser.add_argument("--platform", default="all", help="Target platform (or 'all')")
    parser.add_argument("--output", default=None, help="Output directory (default: ./exports/)")
    parser.add_argument("--json", action="store_true", help="Output report as JSON")
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a valid directory", file=sys.stderr)
        sys.exit(1)

    output_dir = args.output or os.path.join(args.path, "exports")
    files = find_exportable_files(args.path)

    if not files:
        print("No exportable files found.", file=sys.stderr)
        sys.exit(1)

    platforms = list(PLATFORM_CONFIG.keys()) if args.platform == "all" else [args.platform]

    # Validate platform names
    for p in platforms:
        if p not in PLATFORM_CONFIG:
            print(f"Error: Unknown platform '{p}'. Available: {', '.join(PLATFORM_CONFIG.keys())}", file=sys.stderr)
            sys.exit(1)

    results = []
    for platform in platforms:
        result = export_for_platform(args.path, platform, output_dir, files)
        results.append(result)

    report = generate_report(results, args.path)
    print_report(report, json_output=args.json)

    sys.exit(0 if report["total_errors"] == 0 else 1)


if __name__ == "__main__":
    main()
