# Guide Export Cross-Platform — PPG V2

## Vue d'ensemble

Le Premium Project Generator V2 peut exporter les outils Windsurf générés
vers 14+ plateformes IDE. Ce guide documente les formats, les chemins
d'installation, et les adaptateurs automatiques.

## Plateformes supportées

### Tier 1 — Native SKILL.md (copie directe)
Ces plateformes lisent le format SKILL.md nativement. Aucune conversion requise.

| Plateforme | Chemin global | Chemin projet |
|------------|---------------|---------------|
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| GitHub Copilot | `~/.claude/skills/` (partagé) | `.github/skills/` |
| Codex CLI | `~/.agents/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | — |
| Kiro | — | `.kiro/skills/` |
| Antigravity | `~/.agents/skills/` | `.agents/skills/` |
| Goose | `~/.config/goose/skills/` | — |
| OpenCode | `~/.config/opencode/skills/` | — |

### Tier 2 — Auto-adapted (conversion automatique)
Ces plateformes nécessitent une conversion du format SKILL.md.

| Plateforme | Format | Chemin projet | Conversion |
|------------|--------|---------------|------------|
| Cursor | `.mdc` | `.cursor/rules/` | SKILL.md → .mdc (frontmatter adapté) |
| Windsurf | `.md` rule | `.devin/rules/` | SKILL.md → rule avec trigger |
| Cline | plain `.md` | `.clinerules/` | Strip frontmatter |
| Roo Code | plain `.md` | `.roo/rules/` | Strip frontmatter |
| Trae | plain `.md` | `.trae/rules/` | Strip frontmatter |

### Tier 3 — Manual
| Plateforme | Action |
|------------|--------|
| Zed | Copier le corps du skill dans la config Zed |
| Junie | Copier dans le fichier de configuration |
| Aider | Copier dans `.aider.conf.yml` |

## Utilisation du script d'export

```bash
# Export vers toutes les plateformes
python3 tools/scripts/cross-platform-export.py /path/to/kit

# Export vers une plateforme spécifique
python3 tools/scripts/cross-platform-export.py /path/to/kit --platform cursor

# Export avec rapport JSON
python3 tools/scripts/cross-platform-export.py /path/to/kit --json

# Spécifier le dossier de sortie
python3 tools/scripts/cross-platform-export.py /path/to/kit --output ./my-exports/
```

## Format de conversion .mdc (Cursor)

Le format `.mdc` utilisé par Cursor est un frontmatter simplifié :

```yaml
---
description: Description du skill ou de la rule
globs: *.ts,*.tsx
alwaysApply: false
---

[Corps du skill en markdown]
```

L'exporteur convertit automatiquement :
- `name` → ignoré (Cursor utilise le nom de fichier)
- `description` → conservé
- `trigger: glob` → `globs: [extensions du stack]`
- `trigger: always_on` → `alwaysApply: true`
- `trigger: manual` → `alwaysApply: false`

## Chemin universel `~/.agents/skills/`

Convention émergente multi-outils. Un seul install rend le skill
découvrable par Codex CLI, Gemini CLI, Kiro, et Antigravity.

```bash
# Un install, 4+ outils
cp -R ./mon-kit ~/.agents/skills/mon-kit
```

## Bonnes pratiques

1. **Toujours exporter SKILL.md natif** en plus des formats adaptés
2. **Inclure install.sh** dans chaque export pour faciliter l'installation
3. **Documenter** les plateformes cibles dans le README du kit
4. **Tester** l'export sur au moins une plateforme Tier 2 avant livraison
5. **Ne pas exporter** les fichiers de test, memories, ou configs locales
