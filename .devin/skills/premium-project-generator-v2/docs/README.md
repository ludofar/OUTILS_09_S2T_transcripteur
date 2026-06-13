# Premium Project Generator V2 — Documentation

## Vue d'ensemble

Le PPG V2 est un skill Windsurf premium qui génère automatiquement l'intégralité
des outils nécessaires à un projet : AGENTS.md, Rules, Skills, Workflows, RAG, MCP.

**Version** : 2.0.0
**Auteur** : Architecte Système Windsurf Premium

## Nouveautés V2

| # | Fonctionnalité | Description |
|---|---------------|-------------|
| 1 | Security Scan | Scan automatique des livrables (clés, injection, .env) |
| 2 | Staleness Check | Détection d'obsolescence (review dates, deps, drift) |
| 3 | Cross-Platform Export | Export vers Cursor, Claude Code, Copilot, 14+ IDEs |
| 4 | Team Sharing | Auto-push GitHub/GitLab + one-liner d'installation |
| 5 | Discovery Agressive | Clarity Principles (exigences implicites) |
| 6 | Prompts Enrichis | Prompts par niveau avec instructions détaillées |
| 7 | Auto-Install | install.sh cross-workspace (14 plateformes) |
| 8 | Validation Automatisée | Scripts Python remplaçant les checklists manuelles |
| 9 | Registre d'Outils | Catalogue partagé pour les outils d'équipe |
| 10 | Mode Wizard | Configuration pas-à-pas interactive |

## Arborescence

```
premium-project-generator-v2/
├── SKILL.md                    # Définition principale du skill
├── install.sh                  # Installeur cross-workspace
├── docs/
│   └── README.md               # Ce fichier
├── prompts/                    # Prompts meta-prompting (6 fichiers)
│   ├── first-run-init.md
│   ├── level-1-analyzer.md     # + Clarity Principles
│   ├── level-2-architect.md    # + Export planning
│   ├── level-3-generator.md    # + Staleness metadata
│   ├── level-4-validator.md    # + Security + Staleness
│   └── wizard-interactive.md   # Mode wizard (V2)
├── tools/
│   └── scripts/                # Scripts automatisés (V2)
│       ├── security-scan.py
│       ├── staleness-check.py
│       ├── validate-kit.py
│       ├── cross-platform-export.py
│       └── team-registry.py
├── data/
│   ├── config.json             # Configuration V2
│   ├── platform-mappings.json  # Mapping 14+ plateformes (V2)
│   └── stack-mappings.json     # Mapping stack → outils
├── checklists/                 # Checklists qualité (5 fichiers)
│   ├── pre-execution.md
│   ├── post-execution.md
│   ├── quality-checks.md
│   ├── premium-deliverables.md
│   └── security-checks.md     # V2
├── references/                 # Guides de référence (4 fichiers V2)
│   ├── cross-platform-guide.md
│   ├── team-sharing-guide.md
│   ├── security-guide.md
│   └── staleness-guide.md
└── knowledge/
    └── guidelines.md           # Principes architecturaux V2
```

## Utilisation rapide

```
# Lancement standard
@premium-project-generator-v2
  project_name: mon-projet
  tech_stack: nextjs
  business_domain: ecommerce

# Mode wizard
@premium-project-generator-v2 interactive_mode: true

# Avec export et partage
@premium-project-generator-v2
  project_name: mon-projet
  tech_stack: fastapi
  business_domain: fintech
  export_platforms: [windsurf, cursor, claude-code]
  team_sharing: true
```

## Scripts disponibles

```bash
# Validation du kit
python3 tools/scripts/validate-kit.py /path/to/kit

# Scan sécurité
python3 tools/scripts/security-scan.py /path/to/kit

# Détection obsolescence
python3 tools/scripts/staleness-check.py /path/to/kit

# Export cross-platform
python3 tools/scripts/cross-platform-export.py /path/to/kit --platform all

# Registre d'outils
python3 tools/scripts/team-registry.py init --name "Mon Équipe"
python3 tools/scripts/team-registry.py publish ./mon-kit --tags frontend
python3 tools/scripts/team-registry.py list
```

## Installation

```bash
# Copier dans un workspace Windsurf
cp -R premium-project-generator-v2 .devin/skills/premium-project-generator-v2

# Ou utiliser l'installeur
./install.sh                    # Auto-detect
./install.sh --all              # Toutes les plateformes
./install.sh --platform cursor  # Plateforme spécifique
```
