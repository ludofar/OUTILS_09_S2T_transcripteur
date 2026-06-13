#!/usr/bin/env python3
"""
Staleness Checker for Premium Project Generator V2.
Detects outdated tools (Rules, Skills, Workflows) by checking:
- Review dates (last_reviewed vs review_interval_days)
- Dependency health (HTTP check on declared URLs)
- Configuration drift (expected vs actual API responses)

Usage:
    python3 staleness-check.py <path_to_kit>
    python3 staleness-check.py <path_to_kit> --check-deps
    python3 staleness-check.py <path_to_kit> --check-drift
    python3 staleness-check.py <path_to_kit> --json

Exit codes:
    0 = All tools are fresh
    1 = Some tools are overdue for review
    2 = Dependency health issues detected
    3 = Schema drift detected
"""

import argparse
import json
import os
import re
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional


DEFAULT_REVIEW_INTERVAL = 90  # days
STALENESS_THRESHOLDS = {
    "fresh": 0,
    "aging": 60,
    "stale": 90,
    "critical": 180,
}


def parse_frontmatter(filepath: Path) -> Optional[dict]:
    """Extract YAML frontmatter from a markdown file."""
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    # Simple YAML parser for the fields we need (no external deps)
    frontmatter = {}
    current_key = None
    current_list = None

    for line in match.group(1).split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Handle simple key: value
        kv_match = re.match(r"^(\w[\w_-]*)\s*:\s*(.+)$", stripped)
        if kv_match:
            key = kv_match.group(1)
            value = kv_match.group(2).strip().strip("'\"")
            current_key = key
            current_list = None

            if value.lower() in ("true", "false"):
                frontmatter[key] = value.lower() == "true"
            elif value.isdigit():
                frontmatter[key] = int(value)
            elif value == "|" or value == ">-" or value == ">":
                frontmatter[key] = ""
            else:
                frontmatter[key] = value
            continue

        # Handle key: (start of block/list)
        block_match = re.match(r"^(\w[\w_-]*)\s*:\s*$", stripped)
        if block_match:
            current_key = block_match.group(1)
            frontmatter[current_key] = {}
            continue

        # Handle list items
        list_match = re.match(r"^-\s+(.+)$", stripped)
        if list_match and current_key:
            if current_key not in frontmatter or not isinstance(frontmatter[current_key], list):
                frontmatter[current_key] = []
            frontmatter[current_key].append(list_match.group(1).strip().strip("'\""))

    return frontmatter


def get_git_last_modified(filepath: Path) -> Optional[datetime]:
    """Get the last git commit date for a file."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "--", str(filepath)],
            capture_output=True, text=True, timeout=10,
            cwd=str(filepath.parent),
        )
        if result.returncode == 0 and result.stdout.strip():
            date_str = result.stdout.strip()
            return datetime.fromisoformat(date_str.replace("Z", "+00:00")).replace(tzinfo=None)
    except Exception:
        pass
    return None


def check_review_staleness(filepath: Path, frontmatter: dict) -> dict:
    """Check if a tool is overdue for review."""
    now = datetime.now()

    # Try frontmatter metadata first
    last_reviewed = None
    interval = DEFAULT_REVIEW_INTERVAL

    if "metadata" in frontmatter and isinstance(frontmatter["metadata"], dict):
        meta = frontmatter["metadata"]
        if "last_reviewed" in meta:
            try:
                last_reviewed = datetime.strptime(str(meta["last_reviewed"]), "%Y-%m-%d")
            except ValueError:
                pass
        if "review_interval_days" in meta:
            interval = int(meta["review_interval_days"])
    elif "last_reviewed" in frontmatter:
        try:
            last_reviewed = datetime.strptime(str(frontmatter["last_reviewed"]), "%Y-%m-%d")
        except ValueError:
            pass

    if "review_interval_days" in frontmatter:
        interval = int(frontmatter["review_interval_days"])

    # Fallback to git date
    source = "frontmatter"
    if last_reviewed is None:
        last_reviewed = get_git_last_modified(filepath)
        source = "git_commit"

    # Fallback to file mtime
    if last_reviewed is None:
        mtime = os.path.getmtime(filepath)
        last_reviewed = datetime.fromtimestamp(mtime)
        source = "file_mtime"

    days_since = (now - last_reviewed).days
    due_date = last_reviewed + timedelta(days=interval)
    overdue = now > due_date

    if days_since > STALENESS_THRESHOLDS["critical"]:
        status = "CRITICAL"
    elif days_since > STALENESS_THRESHOLDS["stale"]:
        status = "STALE"
    elif days_since > STALENESS_THRESHOLDS["aging"]:
        status = "AGING"
    else:
        status = "FRESH"

    return {
        "file": str(filepath),
        "name": frontmatter.get("name", filepath.stem),
        "last_reviewed": last_reviewed.strftime("%Y-%m-%d"),
        "source": source,
        "interval_days": interval,
        "days_since_review": days_since,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "overdue": overdue,
        "status": status,
    }


def check_dependency_health(frontmatter: dict) -> list[dict]:
    """HTTP-check declared dependency URLs."""
    results = []
    dependencies = frontmatter.get("dependencies", [])

    if isinstance(dependencies, list):
        for dep in dependencies:
            if isinstance(dep, dict) and "url" in dep:
                url = dep["url"]
                name = dep.get("name", url)
                dep_type = dep.get("type", "unknown")
                status = _check_url(url)
                results.append({
                    "name": name,
                    "url": url,
                    "type": dep_type,
                    "reachable": status["ok"],
                    "status_code": status.get("code"),
                    "error": status.get("error"),
                })
            elif isinstance(dep, str) and dep.startswith("http"):
                status = _check_url(dep)
                results.append({
                    "name": dep,
                    "url": dep,
                    "type": "url",
                    "reachable": status["ok"],
                    "status_code": status.get("code"),
                    "error": status.get("error"),
                })

    return results


def _check_url(url: str) -> dict:
    """Check if a URL is reachable using curl."""
    try:
        result = subprocess.run(
            ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "10", url],
            capture_output=True, text=True, timeout=15,
        )
        code = int(result.stdout.strip()) if result.stdout.strip().isdigit() else 0
        return {"ok": 200 <= code < 400, "code": code}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def check_schema_drift(frontmatter: dict) -> list[dict]:
    """Check if API response schemas have drifted from expectations."""
    results = []
    expectations = frontmatter.get("schema_expectations", [])

    if not isinstance(expectations, list):
        return results

    for expectation in expectations:
        if not isinstance(expectation, dict):
            continue

        url = expectation.get("url", "")
        method = expectation.get("method", "GET")
        expected_keys = expectation.get("expected_keys", [])

        if not url or not expected_keys:
            continue

        try:
            result = subprocess.run(
                ["curl", "-sS", "--max-time", "10", "-X", method, url],
                capture_output=True, text=True, timeout=15,
            )
            if result.returncode == 0 and result.stdout:
                try:
                    data = json.loads(result.stdout)
                    if isinstance(data, dict):
                        actual_keys = set(data.keys())
                    elif isinstance(data, list) and data:
                        actual_keys = set(data[0].keys()) if isinstance(data[0], dict) else set()
                    else:
                        actual_keys = set()

                    missing = [k for k in expected_keys if k not in actual_keys]
                    extra = [k for k in actual_keys if k not in expected_keys]

                    results.append({
                        "url": url,
                        "method": method,
                        "expected_keys": expected_keys,
                        "actual_keys": sorted(actual_keys),
                        "missing_keys": missing,
                        "extra_keys": sorted(extra),
                        "drifted": len(missing) > 0,
                    })
                except json.JSONDecodeError:
                    results.append({
                        "url": url,
                        "method": method,
                        "error": "Response is not valid JSON",
                        "drifted": True,
                    })
        except Exception as e:
            results.append({
                "url": url,
                "method": method,
                "error": str(e),
                "drifted": True,
            })

    return results


def find_windsurf_tools(root_path: str) -> list[Path]:
    """Find all Windsurf tool files (Rules, Skills, Workflows)."""
    root = Path(root_path)
    tools = []

    # Skills: .devin/skills/*/SKILL.md
    for skill_md in root.rglob("SKILL.md"):
        tools.append(skill_md)

    # Rules: .devin/rules/*.md
    rules_dir = root / ".devin" / "rules"
    if rules_dir.exists():
        for rule in rules_dir.glob("*.md"):
            tools.append(rule)

    # Workflows: .devin/workflows/*.md
    workflows_dir = root / ".devin" / "workflows"
    if workflows_dir.exists():
        for wf in workflows_dir.glob("*.md"):
            tools.append(wf)

    # Also check root-level SKILL.md, rules, etc.
    for md in root.glob("*.md"):
        if md.name in ("SKILL.md", "AGENTS.md"):
            tools.append(md)

    return list(set(tools))


def generate_report(
    review_results: list[dict],
    dep_results: list[dict],
    drift_results: list[dict],
    root_path: str,
) -> dict[str, Any]:
    """Generate a structured staleness report."""
    overdue = [r for r in review_results if r["overdue"]]
    stale = [r for r in review_results if r["status"] in ("STALE", "CRITICAL")]
    unreachable = [d for d in dep_results if not d["reachable"]]
    drifted = [d for d in drift_results if d.get("drifted")]

    score = 100
    score -= len(overdue) * 10
    score -= len(stale) * 5
    score -= len(unreachable) * 15
    score -= len(drifted) * 10
    score = max(0, score)

    return {
        "scan_date": datetime.now().isoformat(),
        "scanned_path": root_path,
        "staleness_score": score,
        "summary": {
            "total_tools": len(review_results),
            "overdue_for_review": len(overdue),
            "stale_or_critical": len(stale),
            "fresh": len([r for r in review_results if r["status"] == "FRESH"]),
        },
        "dependency_health": {
            "total_checked": len(dep_results),
            "unreachable": len(unreachable),
        },
        "schema_drift": {
            "total_checked": len(drift_results),
            "drifted": len(drifted),
        },
        "review_results": review_results,
        "dependency_results": dep_results,
        "drift_results": drift_results,
    }


def print_report(report: dict, json_output: bool = False) -> None:
    """Print the staleness report."""
    if json_output:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    print("=" * 70)
    print("  STALENESS CHECK REPORT — Premium Project Generator V2")
    print("=" * 70)
    print(f"  Scanned: {report['scanned_path']}")
    print(f"  Date:    {report['scan_date']}")
    print(f"  Score:   {report['staleness_score']}/100")
    print("-" * 70)

    summary = report["summary"]
    print(f"  Tools scanned:      {summary['total_tools']}")
    print(f"  Fresh:              {summary['fresh']}")
    print(f"  Overdue for review: {summary['overdue_for_review']}")
    print(f"  Stale/Critical:     {summary['stale_or_critical']}")
    print("-" * 70)

    if report["review_results"]:
        print(f"\n  {'NAME':<30} {'STATUS':<10} {'DAYS':<6} {'SOURCE':<15} {'INTERVAL':<10}")
        print(f"  {'-'*30} {'-'*10} {'-'*6} {'-'*15} {'-'*10}")
        for r in report["review_results"]:
            icon = {
                "FRESH": "🟢",
                "AGING": "🟡",
                "STALE": "🟠",
                "CRITICAL": "🔴",
            }.get(r["status"], "⚪")
            print(f"  {icon} {r['name']:<28} {r['status']:<10} {r['days_since_review']:<6} {r['source']:<15} {r['interval_days']}d")

    dep_health = report["dependency_health"]
    if dep_health["total_checked"] > 0:
        print(f"\n  Dependencies: {dep_health['total_checked']} checked, {dep_health['unreachable']} unreachable")
        for d in report["dependency_results"]:
            icon = "🟢" if d["reachable"] else "🔴"
            print(f"    {icon} {d['name']} — {d.get('status_code', 'N/A')} {d.get('error', '')}")

    drift = report["schema_drift"]
    if drift["total_checked"] > 0:
        print(f"\n  Schema drift: {drift['total_checked']} checked, {drift['drifted']} drifted")
        for d in report["drift_results"]:
            icon = "🔴" if d.get("drifted") else "🟢"
            missing = d.get("missing_keys", [])
            print(f"    {icon} {d['url']} — missing: {missing if missing else 'none'}")

    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(description="Staleness Checker for PPG V2 generated kits")
    parser.add_argument("path", help="Path to the generated kit or project directory")
    parser.add_argument("--check-deps", action="store_true", help="Check dependency URL health")
    parser.add_argument("--check-drift", action="store_true", help="Check API schema drift")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a valid directory", file=sys.stderr)
        sys.exit(1)

    tool_files = find_windsurf_tools(args.path)
    review_results = []
    dep_results = []
    drift_results = []

    for tool_file in tool_files:
        frontmatter = parse_frontmatter(tool_file)
        if frontmatter is None:
            continue

        review_results.append(check_review_staleness(tool_file, frontmatter))

        if args.check_deps:
            dep_results.extend(check_dependency_health(frontmatter))

        if args.check_drift:
            drift_results.extend(check_schema_drift(frontmatter))

    report = generate_report(review_results, dep_results, drift_results, args.path)
    print_report(report, json_output=args.json)

    if report["schema_drift"]["drifted"] > 0:
        sys.exit(3)
    elif report["dependency_health"]["unreachable"] > 0:
        sys.exit(2)
    elif report["summary"]["overdue_for_review"] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
