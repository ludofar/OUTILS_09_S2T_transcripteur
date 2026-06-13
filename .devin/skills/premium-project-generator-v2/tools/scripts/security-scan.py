#!/usr/bin/env python3
"""
Security Scanner for Premium Project Generator V2.
Scans generated Windsurf tools (Rules, Skills, Workflows, configs)
for hardcoded secrets, injection patterns, and exposed credentials.

Usage:
    python3 security-scan.py <path_to_kit>
    python3 security-scan.py <path_to_kit> --json
    python3 security-scan.py <path_to_kit> --fix

Exit codes:
    0 = No issues found
    1 = Warnings found (medium severity)
    2 = Critical issues found (high severity, blocks delivery)
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


SEVERITY_HIGH = "HIGH"
SEVERITY_MEDIUM = "MEDIUM"
SEVERITY_LOW = "LOW"
SEVERITY_INFO = "INFO"

SECRET_PATTERNS = [
    {
        "name": "AWS Access Key",
        "pattern": r"(?:AKIA|ASIA)[A-Z0-9]{16}",
        "severity": SEVERITY_HIGH,
        "description": "AWS Access Key ID detected",
    },
    {
        "name": "AWS Secret Key",
        "pattern": r"(?:aws_secret_access_key|aws_secret)\s*[=:]\s*['\"]?[A-Za-z0-9/+=]{40}",
        "severity": SEVERITY_HIGH,
        "description": "AWS Secret Access Key detected",
    },
    {
        "name": "Generic API Key",
        "pattern": r"(?:api[_-]?key|apikey|api[_-]?secret)\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{20,}['\"]?",
        "severity": SEVERITY_HIGH,
        "description": "Generic API key pattern detected",
    },
    {
        "name": "Bearer Token",
        "pattern": r"['\"]Bearer\s+[A-Za-z0-9_\-\.]{20,}['\"]",
        "severity": SEVERITY_HIGH,
        "description": "Bearer token hardcoded",
    },
    {
        "name": "Private Key",
        "pattern": r"-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----",
        "severity": SEVERITY_HIGH,
        "description": "Private key embedded in file",
    },
    {
        "name": "GitHub Token",
        "pattern": r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,}",
        "severity": SEVERITY_HIGH,
        "description": "GitHub personal access token detected",
    },
    {
        "name": "Slack Token",
        "pattern": r"xox[bporas]-[A-Za-z0-9\-]{10,}",
        "severity": SEVERITY_HIGH,
        "description": "Slack token detected",
    },
    {
        "name": "Generic Password",
        "pattern": r"(?:password|passwd|pwd|secret)\s*[=:]\s*['\"][^'\"]{8,}['\"]",
        "severity": SEVERITY_MEDIUM,
        "description": "Hardcoded password pattern detected",
    },
    {
        "name": "Database URL with credentials",
        "pattern": r"(?:postgres|mysql|mongodb|redis)://[^:]+:[^@]+@",
        "severity": SEVERITY_HIGH,
        "description": "Database connection string with credentials",
    },
    {
        "name": "Env file reference without gitignore",
        "pattern": r"\.env(?:\.local|\.production|\.staging)?",
        "severity": SEVERITY_LOW,
        "description": "Reference to .env file — ensure it is gitignored",
    },
]

INJECTION_PATTERNS = [
    {
        "name": "Shell injection",
        "pattern": r"(?:os\.system|subprocess\.call|subprocess\.run|exec)\s*\([^)]*\$\{",
        "severity": SEVERITY_MEDIUM,
        "description": "Potential shell injection via variable interpolation",
    },
    {
        "name": "eval() usage",
        "pattern": r"\beval\s*\(",
        "severity": SEVERITY_MEDIUM,
        "description": "eval() usage detected — potential code injection",
    },
    {
        "name": "SQL injection",
        "pattern": r"(?:execute|query)\s*\([^)]*['\"].*\+.*(?:request|input|param|user)",
        "severity": SEVERITY_MEDIUM,
        "description": "Potential SQL injection via string concatenation",
    },
    {
        "name": "Template injection",
        "pattern": r"\{\{.*(?:request|input|user|param).*\}\}",
        "severity": SEVERITY_LOW,
        "description": "Potential template injection",
    },
]

CONFIG_PATTERNS = [
    {
        "name": "Token in MCP config",
        "pattern": r"(?:\"token\"|\"secret\"|\"api_key\")\s*:\s*\"[^\"]{10,}\"",
        "severity": SEVERITY_HIGH,
        "description": "Token/secret in MCP or integration config (use env vars)",
    },
    {
        "name": "Hardcoded URL with auth",
        "pattern": r"https?://[^:]+:[^@]+@",
        "severity": SEVERITY_MEDIUM,
        "description": "URL with embedded credentials",
    },
    {
        "name": "Debug mode enabled",
        "pattern": r"(?:\"debug\"|debug)\s*[=:]\s*(?:true|True|1)",
        "severity": SEVERITY_LOW,
        "description": "Debug mode is enabled — disable for production",
    },
]

SCAN_EXTENSIONS = {
    ".md", ".yaml", ".yml", ".json", ".js", ".ts", ".py", ".sh",
    ".mdc", ".toml", ".cfg", ".ini", ".env", ".conf",
}

SKIP_DIRS = {
    "node_modules", ".git", "__pycache__", ".venv", "venv",
    "dist", "build", ".next", ".nuxt",
}


def find_files(root_path: str) -> list[Path]:
    """Find all scannable files in the kit directory."""
    files = []
    root = Path(root_path)
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in SCAN_EXTENSIONS:
            if not any(skip in path.parts for skip in SKIP_DIRS):
                files.append(path)
    return files


def scan_file(filepath: Path, patterns: list[dict]) -> list[dict]:
    """Scan a single file against a list of patterns."""
    findings = []
    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return findings

    lines = content.split("\n")
    for i, line in enumerate(lines, 1):
        # Skip comments explaining patterns (e.g., documentation about what to avoid)
        stripped = line.strip()
        if stripped.startswith("#") or stripped.startswith("//") or stripped.startswith("<!--"):
            continue

        for pattern_def in patterns:
            matches = re.finditer(pattern_def["pattern"], line, re.IGNORECASE)
            for match in matches:
                # Mask the actual secret in the report
                matched_text = match.group(0)
                masked = matched_text[:8] + "..." + matched_text[-4:] if len(matched_text) > 16 else "***"
                findings.append({
                    "file": str(filepath),
                    "line": i,
                    "rule": pattern_def["name"],
                    "severity": pattern_def["severity"],
                    "description": pattern_def["description"],
                    "match_preview": masked,
                })
    return findings


def check_env_files(root_path: str) -> list[dict]:
    """Check for exposed .env files and missing .gitignore entries."""
    findings = []
    root = Path(root_path)

    env_files = list(root.rglob(".env*"))
    gitignore_path = root / ".gitignore"

    gitignore_content = ""
    if gitignore_path.exists():
        gitignore_content = gitignore_path.read_text(encoding="utf-8", errors="replace")

    for env_file in env_files:
        if env_file.name == ".env.example" or env_file.name == ".env.template":
            continue
        rel = str(env_file.relative_to(root))
        if rel not in gitignore_content and ".env" not in gitignore_content:
            findings.append({
                "file": str(env_file),
                "line": 0,
                "rule": "Exposed .env file",
                "severity": SEVERITY_HIGH,
                "description": f"{rel} exists but is not in .gitignore",
                "match_preview": rel,
            })
    return findings


def generate_report(findings: list[dict], root_path: str) -> dict[str, Any]:
    """Generate a structured security report."""
    high = [f for f in findings if f["severity"] == SEVERITY_HIGH]
    medium = [f for f in findings if f["severity"] == SEVERITY_MEDIUM]
    low = [f for f in findings if f["severity"] == SEVERITY_LOW]

    total = len(findings)
    score = 100
    score -= len(high) * 15
    score -= len(medium) * 5
    score -= len(low) * 1
    score = max(0, score)

    return {
        "scan_date": datetime.now().isoformat(),
        "scanned_path": root_path,
        "total_findings": total,
        "by_severity": {
            "HIGH": len(high),
            "MEDIUM": len(medium),
            "LOW": len(low),
        },
        "security_score": score,
        "pass": len(high) == 0,
        "findings": findings,
        "recommendations": _generate_recommendations(findings),
    }


def _generate_recommendations(findings: list[dict]) -> list[str]:
    """Generate actionable recommendations based on findings."""
    recs = []
    rules_found = {f["rule"] for f in findings}

    if any("API" in r or "Token" in r or "Key" in r for r in rules_found):
        recs.append("Use environment variables for all API keys and tokens. Reference them as ${ENV_VAR} in configs.")
    if "Exposed .env file" in rules_found:
        recs.append("Add .env* to .gitignore immediately. Use .env.example for templates.")
    if any("injection" in r.lower() for r in rules_found):
        recs.append("Sanitise all user inputs before passing to shell commands, SQL queries, or template engines.")
    if any("password" in r.lower() for r in rules_found):
        recs.append("Never hardcode passwords. Use a secrets manager or environment variables.")
    if "Debug mode enabled" in rules_found:
        recs.append("Disable debug mode in production configurations.")
    if any("Private Key" in r for r in rules_found):
        recs.append("Remove private keys from the repository. Store them in a secure vault.")
    if not recs:
        recs.append("No specific recommendations — the kit passes security checks.")

    return recs


def print_report(report: dict, json_output: bool = False) -> None:
    """Print the security report."""
    if json_output:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return

    print("=" * 60)
    print("  SECURITY SCAN REPORT — Premium Project Generator V2")
    print("=" * 60)
    print(f"  Scanned: {report['scanned_path']}")
    print(f"  Date:    {report['scan_date']}")
    print(f"  Score:   {report['security_score']}/100")
    print(f"  Status:  {'PASS' if report['pass'] else 'FAIL — HIGH severity issues found'}")
    print("-" * 60)
    print(f"  HIGH:   {report['by_severity']['HIGH']}")
    print(f"  MEDIUM: {report['by_severity']['MEDIUM']}")
    print(f"  LOW:    {report['by_severity']['LOW']}")
    print("-" * 60)

    if report["findings"]:
        print("\nFindings:\n")
        for f in report["findings"]:
            icon = "🔴" if f["severity"] == SEVERITY_HIGH else "🟡" if f["severity"] == SEVERITY_MEDIUM else "🔵"
            print(f"  {icon} [{f['severity']}] {f['rule']}")
            print(f"     File: {f['file']}:{f['line']}")
            print(f"     {f['description']}")
            print()

    if report["recommendations"]:
        print("Recommendations:\n")
        for i, rec in enumerate(report["recommendations"], 1):
            print(f"  {i}. {rec}")
        print()

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Security Scanner for PPG V2 generated kits")
    parser.add_argument("path", help="Path to the generated kit directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fix", action="store_true", help="Attempt auto-fix (add .gitignore entries)")
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a valid directory", file=sys.stderr)
        sys.exit(1)

    files = find_files(args.path)
    all_findings = []

    all_patterns = SECRET_PATTERNS + INJECTION_PATTERNS + CONFIG_PATTERNS
    for f in files:
        all_findings.extend(scan_file(f, all_patterns))

    all_findings.extend(check_env_files(args.path))

    report = generate_report(all_findings, args.path)
    print_report(report, json_output=args.json)

    if args.fix:
        _auto_fix(args.path, all_findings)

    if report["by_severity"]["HIGH"] > 0:
        sys.exit(2)
    elif report["by_severity"]["MEDIUM"] > 0:
        sys.exit(1)
    sys.exit(0)


def _auto_fix(root_path: str, findings: list[dict]) -> None:
    """Attempt automatic fixes for common issues."""
    root = Path(root_path)
    gitignore_path = root / ".gitignore"
    env_issues = [f for f in findings if f["rule"] == "Exposed .env file"]

    if env_issues:
        entries = [".env", ".env.local", ".env.production", ".env.staging", ".env.*", "!.env.example"]
        existing = ""
        if gitignore_path.exists():
            existing = gitignore_path.read_text(encoding="utf-8")

        new_entries = [e for e in entries if e not in existing]
        if new_entries:
            with open(gitignore_path, "a", encoding="utf-8") as f:
                f.write("\n# Security: auto-added by PPG V2 security scan\n")
                for entry in new_entries:
                    f.write(f"{entry}\n")
            print(f"\n  Auto-fix: Added {len(new_entries)} entries to .gitignore")


if __name__ == "__main__":
    main()
