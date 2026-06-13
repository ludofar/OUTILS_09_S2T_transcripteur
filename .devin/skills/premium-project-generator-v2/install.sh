#!/bin/sh
# Premium Project Generator V2 — Cross-Workspace Installer
# Installs or symlinks this skill to any Windsurf workspace or global path.
#
# Usage:
#   ./install.sh                      # Auto-detect and install
#   ./install.sh --target /path/to/project
#   ./install.sh --global             # Install to global Windsurf path
#   ./install.sh --all                # Install to all detected platforms
#   ./install.sh --dry-run            # Preview without changes
#   ./install.sh --uninstall          # Remove installed symlinks
#   ./install.sh --platform cursor    # Install for specific platform

set -e

SKILL_NAME="premium-project-generator-v2"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DRY_RUN=0
UNINSTALL=0
GLOBAL=0
ALL=0
TARGET=""
PLATFORM=""

# Parse arguments
while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run)    DRY_RUN=1 ;;
        --uninstall)  UNINSTALL=1 ;;
        --global)     GLOBAL=1 ;;
        --all)        ALL=1 ;;
        --target)     shift; TARGET="$1" ;;
        --platform)   shift; PLATFORM="$1" ;;
        -h|--help)
            echo "Usage: $0 [options]"
            echo "  --target <path>   Install to specific project workspace"
            echo "  --global          Install to global Windsurf config"
            echo "  --all             Install to all detected platforms"
            echo "  --platform <name> Install for specific platform"
            echo "  --dry-run         Preview without making changes"
            echo "  --uninstall       Remove installed symlinks/copies"
            echo ""
            echo "Supported platforms: windsurf, cursor, claude-code, copilot,"
            echo "  codex, gemini, kiro, trae, goose, opencode, roo-code,"
            echo "  cline, antigravity, universal"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
    shift
done

log() {
    echo "  $1"
}

install_to() {
    local dest="$1"
    local label="$2"

    if [ "$UNINSTALL" = "1" ]; then
        if [ -e "$dest" ] || [ -L "$dest" ]; then
            if [ "$DRY_RUN" = "1" ]; then
                log "[DRY-RUN] Would remove: $dest"
            else
                rm -rf "$dest"
                log "Removed: $dest ($label)"
            fi
        else
            log "Not found: $dest ($label) — skipped"
        fi
        return
    fi

    if [ "$DRY_RUN" = "1" ]; then
        log "[DRY-RUN] Would install to: $dest ($label)"
        return
    fi

    # Create parent directory
    mkdir -p "$(dirname "$dest")"

    # Remove existing if present
    [ -e "$dest" ] && rm -rf "$dest"

    # Try symlink first, fall back to copy
    if ln -s "$SCRIPT_DIR" "$dest" 2>/dev/null; then
        log "Symlinked: $dest ($label)"
    else
        cp -R "$SCRIPT_DIR" "$dest"
        log "Copied: $dest ($label)"
    fi
}

detect_and_install_windsurf() {
    # Project-level
    if [ -n "$TARGET" ]; then
        install_to "$TARGET/.devin/skills/$SKILL_NAME" "Windsurf project ($TARGET)"
    elif [ -d ".devin" ]; then
        install_to ".devin/skills/$SKILL_NAME" "Windsurf project (current)"
    fi

    # Global
    if [ "$GLOBAL" = "1" ] || [ "$ALL" = "1" ]; then
        local global_path=""
        if [ -d "$HOME/.codeium/windsurf" ]; then
            global_path="$HOME/.codeium/windsurf/skills/$SKILL_NAME"
        fi
        if [ -n "$global_path" ]; then
            install_to "$global_path" "Windsurf global"
        fi
    fi
}

detect_and_install_cursor() {
    if [ -d ".cursor" ] || [ "$ALL" = "1" ]; then
        install_to ".cursor/rules/$SKILL_NAME" "Cursor project"
    fi
}

detect_and_install_claude() {
    if [ -d "$HOME/.claude" ] || [ "$ALL" = "1" ]; then
        install_to "$HOME/.claude/skills/$SKILL_NAME" "Claude Code global"
    fi
}

detect_and_install_copilot() {
    if [ -d ".github" ] || [ "$ALL" = "1" ]; then
        install_to ".github/skills/$SKILL_NAME" "GitHub Copilot project"
    fi
}

detect_and_install_universal() {
    install_to "$HOME/.agents/skills/$SKILL_NAME" "Universal path"
}

detect_and_install_gemini() {
    if [ -d "$HOME/.gemini" ] || [ "$ALL" = "1" ]; then
        install_to "$HOME/.gemini/skills/$SKILL_NAME" "Gemini CLI global"
    fi
}

detect_and_install_kiro() {
    if [ -d ".kiro" ] || [ "$ALL" = "1" ]; then
        install_to ".kiro/skills/$SKILL_NAME" "Kiro project"
    fi
}

detect_and_install_trae() {
    if [ -d ".trae" ] || [ "$ALL" = "1" ]; then
        install_to ".trae/rules/$SKILL_NAME" "Trae project"
    fi
}

detect_and_install_cline() {
    if [ -d ".clinerules" ] || [ "$ALL" = "1" ]; then
        install_to ".clinerules/$SKILL_NAME" "Cline project"
    fi
}

detect_and_install_roo() {
    if [ -d ".roo" ] || [ "$ALL" = "1" ]; then
        install_to ".roo/rules/$SKILL_NAME" "Roo Code project"
    fi
}

detect_and_install_goose() {
    if [ -d "$HOME/.config/goose" ] || [ "$ALL" = "1" ]; then
        install_to "$HOME/.config/goose/skills/$SKILL_NAME" "Goose global"
    fi
}

detect_and_install_opencode() {
    if [ -d "$HOME/.config/opencode" ] || [ "$ALL" = "1" ]; then
        install_to "$HOME/.config/opencode/skills/$SKILL_NAME" "OpenCode global"
    fi
}

# Main
echo ""
echo "  Premium Project Generator V2 — Installer"
echo "  =========================================="
echo ""

if [ -n "$PLATFORM" ]; then
    case "$PLATFORM" in
        windsurf)       detect_and_install_windsurf ;;
        cursor)         detect_and_install_cursor ;;
        claude-code)    detect_and_install_claude ;;
        copilot)        detect_and_install_copilot ;;
        codex)          detect_and_install_universal ;;
        gemini)         detect_and_install_gemini ;;
        kiro)           detect_and_install_kiro ;;
        trae)           detect_and_install_trae ;;
        cline)          detect_and_install_cline ;;
        roo-code)       detect_and_install_roo ;;
        goose)          detect_and_install_goose ;;
        opencode)       detect_and_install_opencode ;;
        antigravity)    detect_and_install_universal ;;
        universal)      detect_and_install_universal ;;
        *)
            echo "  Unknown platform: $PLATFORM"
            exit 1
            ;;
    esac
elif [ "$ALL" = "1" ]; then
    detect_and_install_windsurf
    detect_and_install_cursor
    detect_and_install_claude
    detect_and_install_copilot
    detect_and_install_universal
    detect_and_install_gemini
    detect_and_install_kiro
    detect_and_install_trae
    detect_and_install_cline
    detect_and_install_roo
    detect_and_install_goose
    detect_and_install_opencode
else
    # Auto-detect
    detect_and_install_windsurf
    [ -d ".cursor" ]                    && detect_and_install_cursor
    [ -d "$HOME/.claude" ]              && detect_and_install_claude
    [ -d ".github" ]                    && detect_and_install_copilot
    [ -d "$HOME/.gemini" ]              && detect_and_install_gemini
    [ -d ".kiro" ]                      && detect_and_install_kiro
    [ -d ".trae" ]                      && detect_and_install_trae
    [ -d ".clinerules" ]                && detect_and_install_cline
    [ -d ".roo" ]                       && detect_and_install_roo
    [ -d "$HOME/.config/goose" ]        && detect_and_install_goose
    [ -d "$HOME/.config/opencode" ]     && detect_and_install_opencode

    # Always install to universal path
    detect_and_install_universal
fi

echo ""
echo "  Done. Invoke with @premium-project-generator-v2"
echo ""
