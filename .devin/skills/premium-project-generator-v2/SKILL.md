---
name: premium-project-generator-v2
description: |
  Skill PREMIUM V2 pour générer automatiquement l'intégralité des outils Windsurf
  nécessaires à tout projet : AGENTS.md, Rules, Skills, Workflows, MCP, RAG.
  Utilise un meta-prompting hiérarchique à 4 niveaux (Analyseur → Architecte →
  Générateur → Validateur) avec Security Scan et Staleness Check intégrés.
  Adaptatif selon le stack, le domaine métier, la taille d'équipe et la maturité.
  Export cross-platform (Cursor, Claude Code, Copilot, Codex CLI, Gemini CLI).
  Partage équipe auto GitHub/GitLab. Mode wizard interactif. Registre d'outils.
  
  Invoqué pour : création de projet, setup d'environnement, génération d'outils
  Windsurf premium, architecture de skills multi-étapes, configuration RAG/MCP,
  export cross-platform, partage équipe, audit sécurité, détection obsolescence.
version: 2.0.0
author: Architecte Système Windsurf Premium
tags:
  - premium
  - project-generator
  - meta-prompting
  - windsurf-tools
  - rag
  - mcp
  - automation
  - security-scan
  - staleness-check
  - cross-platform
  - team-sharing
  - wizard
category: Architecture
scope: workspace
prerequisites:
  - Windsurf IDE avec Cascade
  - Connaissance basique du projet (stack, domaine, contraintes)
  - Droit d'écriture dans le workspace
  - Node.js 18+ (si scripts utilisés)
  - Python 3.8+ (pour security scan, staleness check, validation)
dependencies:
  - project-context-analyzer
  - docs-auto-updater
  - tools-documentation
  - specification-brainstorm
triggers:
  - generate project tools
  - create windsurf setup
  - bootstrap project
  - setup windsurf
  - generate skills
  - create rules
  - project initialization
  - windsurf premium
  - export tools
  - share with team
  - security audit
  - check staleness
  - interactive wizard
inputs:
  project_name:
    type: string
    required: true
    description: "Nom du projet en kebab-case"
  tech_stack:
    type: string
    required: true
    description: "Stack technique (ex: Next.js/TS, Python/FastAPI, Rust/Tauri)"
  business_domain:
    type: string
    required: true
    description: "Domaine métier (ex: fintech, santé, e-commerce, IoT)"
  team_size:
    type: string
    required: false
    default: "small"
    enum: ["solo", "small", "medium", "large"]
    description: "Taille de l'équipe"
  maturity:
    type: string
    required: false
    default: "MVP"
    enum: ["POC", "MVP", "production", "legacy-migration"]
    description: "Maturité du projet"
  constraints:
    type: array
    required: false
    description: "Contraintes (perf, RGPD, a11y, i18n, sécurité...)"
  languages:
    type: array
    required: false
    default: ["fr"]
    description: "Langues cibles"
  export_platforms:
    type: array
    required: false
    default: ["windsurf"]
    description: "Plateformes cibles pour export (windsurf, cursor, claude-code, copilot, codex, gemini, universal)"
  team_sharing:
    type: boolean
    required: false
    default: false
    description: "Activer le partage équipe automatique GitHub/GitLab"
  interactive_mode:
    type: boolean
    required: false
    default: false
    description: "Activer le wizard interactif pas-à-pas"
outputs:
  agents_md:
    type: string
    description: "AGENTS.md hiérarchiques générés"
  rules_set:
    type: array
    description: "Set de Rules adaptatives"
  skills_set:
    type: array
    description: "Skills multi-étapes complets"
  workflows_set:
    type: array
    description: "Workflows manuels"
  rag_config:
    type: object
    description: "Configuration RAG du projet"
  mcp_config:
    type: object
    description: "Configuration MCP du projet"
  tools_guide:
    type: string
    description: "TOOLS_USERGUIDE.md généré"
  security_report:
    type: object
    description: "Rapport de scan sécurité des livrables"
  staleness_report:
    type: object
    description: "Rapport d'obsolescence des outils"
  export_packages:
    type: array
    description: "Packages exportés par plateforme cible"
auto_invoke: false
confidence_threshold: 0.8
rag_sources: ["local", "remote"]
mcp_servers: ["filesystem"]
---

# Premium Project Generator V2

## Vue d'ensemble

Ce skill **PREMIUM V2** est le cœur du système d'outillage Windsurf. Il génère
automatiquement et intelligemment l'intégralité des outils nécessaires à tout
projet, quelle que soit sa taille ou sa complexité.

**Nouveautés V2** (10 améliorations issues de l'analyse d'`agent-skill-creator`) :
1. **Security Scan intégré** — Scan automatique des livrables générés (clés hardcodées, injection, .env exposés)
2. **Staleness Check** — Détection d'obsolescence des outils (review dates, deps health, schema drift)
3. **Export cross-platform** — Export vers Cursor (.mdc), Claude Code, Copilot, Codex CLI, Gemini CLI, 14+ outils
4. **Partage équipe** — Auto-push GitHub/GitLab avec one-liner d'installation
5. **Discovery agressive** — Clarity Principles : va au-delà de la description utilisateur
6. **Prompts enrichis** — Prompts externalisés par niveau avec instructions détaillées
7. **Auto-install universel** — `install.sh` pour distribuer le skill sur n'importe quel workspace
8. **Scripts validation exécutables** — Remplace les checklists manuelles par des scripts automatisés
9. **Registre d'outils d'équipe** — Catalogue partagé pour les outils Windsurf générés
10. **Mode wizard interactif** — Configuration pas-à-pas pour utilisateurs non techniques

**Valeur unique** :
- **First-Run Auto-Init** : À sa première exécution dans un workspace, il déploie
  automatiquement les 3 skills de base fondamentaux
- **Meta-prompting à 4 niveaux** + Security Gate : Analyseur → Architecte → Générateur → Validateur+Security
- **Contexte auto-détecté** : Lecture du rapport `@project-context-analyzer`
- **Cross-platform** : Un kit Windsurf exportable sur 14+ plateformes

**Tarification de référence** : 2500€ (valeur augmentée par les 10 améliorations V2).

## Ce que fait ce skill à sa première lancée (First-Run)

Quand vous copiez ce skill dans un projet et que vous invoquez
`@premium-project-generator-v2` pour la **toute première fois**, voici la séquence
exacte qui s'exécute **automatiquement** :

### 1. Détection du First-Run
Le skill vérifie si les skills fondamentaux existent déjà dans `.devin/skills/`.
S'ils sont absents, il bascule en mode **First-Run Auto-Init**.

### 2. Déploiement des 3 skills de base

#### A. `@specification-brainstorm` (Atelier cahier des charges)
- **Fichier créé** : `.devin/skills/specification-brainstorm/SKILL.md`
- **Fonction** : Guider l'utilisateur dans la rédaction d'un cahier des charges
  structuré, avec mémoire persistante des décisions
- **Workflow associé** : `/brainstorm` (`.devin/workflows/meta-brainstorm.md`)

#### B. `@docs-auto-updater` (Synchronisation documentation)
- **Fichier créé** : `.devin/skills/docs-auto-updater/SKILL.md`
- **Fonction** : Scanner l'arborescence `.devin/`, détecter les écarts entre
  le code et la documentation, et proposer des mises à jour automatiques
- **Workflow associé** : `/update-docs` (`.devin/workflows/update-tools-docs.md`)

#### C. **Meta-prompting à 4 niveaux** (Système principal)
- **Vérification** : Les 5 prompts existent déjà dans `prompts/level-*.md`
- **Workflow associé** : `/init-project` (`.devin/workflows/init-project.md`)

### 3. Phase Discovery Agressive (Clarity Principles — V2)

**Principe fondamental** : Les utilisateurs décrivent ce qu'ils *font*, pas ce qu'ils
*ont besoin*. Le Discovery V2 va au-delà de la description de surface.

- Le skill tente de lire `data/context-report.json` produit par
  `@project-context-analyzer` (si disponible)
- S'il est présent et que `confidence_score >= 80` : les inputs sont pré-remplis
- **Clarity Principles** (nouveauté V2) :
  1. **Lire tout avant de conclure** — Consommer tout le matériel disponible (README, configs, code, .devin/) avant de former une opinion
  2. **Challenger la description** — L'input utilisateur est un point de départ, pas une spécification. Identifier les manques, les implicites, les contradictions
  3. **Extraire les exigences implicites** — Error handling, edge cases, contraintes réglementaires que l'utilisateur assume évidentes
  4. **Identifier le vrai besoin** — "Je veux un setup Windsurf" cache : pour qui ? quels processus ? quelle fréquence de mise à jour ? quels garde-fous ?
  5. **Surpasser la compréhension utilisateur** — La spécification produite doit contenir des exigences que l'utilisateur dirait "oui, exactement" — mais n'aurait jamais pu articuler
- Sinon : 3 questions maximum, mais formulées avec les Clarity Principles

### 4. Lancement du meta-prompting principal
Les 4 niveaux s'exécutent séquentiellement :
1. **Analyseur** (Niveau 1) : Diagnostic et rapport d'analyse + Clarity Principles
2. **Architecte** (Niveau 2) : Blueprint technique des outils à générer
3. **Générateur** (Niveau 3) : Production concrète des fichiers
4. **Validateur** (Niveau 4) : Quality gate + **Security Scan** + **Staleness Check**

### 5. Finalisation et synchronisation
- Génération de `TOOLS_USERGUIDE.md`
- **Security Scan** automatique de tous les livrables (V2)
- **Staleness metadata** injectée dans chaque livrable (V2)
- **Export cross-platform** si `export_platforms` spécifié (V2)
- **Partage équipe** si `team_sharing` activé (V2)
- **Appel automatique** à `@docs-auto-updater`
- Mise à jour des mémoires

### Récapitulatif First-Run V2
| Élément | Quantité | Détail |
|---------|----------|--------|
| Skills fondamentaux | 3 | `specification-brainstorm`, `docs-auto-updater`, `premium-project-generator-v2` |
| Workflows | 4 | `/init-project`, `/brainstorm`, `/update-docs`, `/wizard` (V2) |
| Livrables générés | 10+ | AGENTS.md, 4+ Rules, 3+ Skills, 3+ Workflows, RAG, MCP |
| Rapports V2 | 3 | Security report, Staleness report, Validation report |
| Exports V2 | 1-14 | Packages cross-platform si demandé |
| Documentation | 3+ | TOOLS_USERGUIDE.md, README, memories, CHANGELOG |

## Cas d'usage

1. **Bootstrap projet (First-Run)** : `@premium-project-generator-v2` auto-initie tout
2. **Migration legacy** : Moderniser les outils d'un projet existant
3. **Scaling équipe** : Générer rules et skills adaptés + partage équipe (V2)
4. **Audit & refonte** : Analyser avec Security Scan + Staleness Check (V2)
5. **Export multi-IDE** : Exporter le kit vers Cursor, Claude Code, Copilot (V2)
6. **Formation** : Mode wizard interactif pour utilisateurs non techniques (V2)
7. **Registre centralisé** : Catalogue d'outils partagé dans l'organisation (V2)

## Procédure pas à pas (Meta-Prompting 4 Niveaux + Security Gate)

### Phase 0 : Discovery Agressive (Cadrage V2)

**Automatique via @project-context-analyzer + Clarity Principles** :
1. **Vérifier** si `data/context-report.json` existe
2. **Si oui** :
   - Charger le rapport et extraire les variables
   - Si `confidence_score >= 80` : utiliser directement, passer à Phase 0b
   - Si `confidence_score < 80` : présenter pour validation rapide
3. **Si non** : scanner le workspace directement :
   - Lire `package.json`, `requirements.txt`, `pubspec.yaml`, `Cargo.toml`, etc.
   - Lire `.devin/`, `.github/`, `.cursor/` existants
   - Analyser la structure de fichiers et les patterns
4. **Appliquer les Clarity Principles** :
   - Identifier les exigences implicites du domaine
   - Détecter les contradictions entre l'input et le code existant
   - Formuler les questions non évidentes que l'utilisateur n'a pas posées
   - Générer une spec interne plus riche que l'input
5. **Si mode wizard** (`interactive_mode: true`) : lancer le wizard interactif
   - Voir `prompts/wizard-interactive.md`

### Phase 0b : First-Run Auto-Initialization

*Identique à V1 — voir `prompts/first-run-init.md`*

### Phase 1 : ANALYSEUR (Niveau 1)

**Objectif** : Diagnostiquer le besoin avec les Clarity Principles

1. **Charger** le prompt `prompts/level-1-analyzer.md`
2. **Analyser** les inputs avec extraction d'exigences implicites (V2)
3. **Produire** `data/analysis-report.json`

### Phase 2 : ARCHITECTE (Niveau 2)

**Objectif** : Transformer l'analyse en blueprint technique

1. **Charger** le prompt `prompts/level-2-architect.md`
2. **Concevoir** l'architecture incluant export cross-platform (V2)
3. **Produire** `data/architecture-blueprint.json`

### Phase 3 : GÉNÉRATEUR (Niveau 3)

**Objectif** : Produire tous les fichiers concrets

1. **Charger** le prompt `prompts/level-3-generator.md`
2. **Générer** dans l'ordre strict (identique V1)
3. **Injecter** les métadonnées de staleness dans chaque livrable (V2) :
   ```yaml
   metadata:
     created: YYYY-MM-DD
     last_reviewed: YYYY-MM-DD
     review_interval_days: 90
   ```

### Phase 4 : VALIDATEUR + SECURITY GATE (Niveau 4 — V2)

**Objectif** : Quality gate + Security Scan + Staleness Check

1. **Charger** le prompt `prompts/level-4-validator.md`
2. **Validation structurelle** (identique V1)
3. **Security Scan** (nouveauté V2) :
   - Exécuter `python3 tools/scripts/security-scan.py` sur chaque livrable
   - Détecter : clés API hardcodées, patterns d'injection, .env exposés, tokens en clair
   - Bloquer la livraison si sévérité HIGH détectée
4. **Staleness Check** (nouveauté V2) :
   - Exécuter `python3 tools/scripts/staleness-check.py` sur le kit
   - Vérifier : dates de review, santé des dépendances, drift de configuration
   - Reporter les outils à risque d'obsolescence
5. **Scoring enrichi** (0-100) :
   - Complétude livrables (25 points)
   - Qualité frontmatter (15 points)
   - Cohérence inter-fichiers (15 points)
   - Exemples et documentation (15 points)
   - Standards premium (10 points)
   - **Security Score** (10 points) — V2
   - **Staleness Score** (10 points) — V2

### Phase 5 : Finalisation + Export + Partage (V2)

1. **Générer** `TOOLS_USERGUIDE.md`
2. **Invoquer** `@docs-auto-updater`
3. **Export cross-platform** (V2) si `export_platforms` défini :
   - Exécuter `python3 tools/scripts/cross-platform-export.py`
   - Générer les adaptateurs par plateforme (`.mdc` pour Cursor, `SKILL.md` natif pour Claude Code, etc.)
   - Voir `references/cross-platform-guide.md`
4. **Partage équipe** (V2) si `team_sharing: true` :
   - Auto-détecter GitHub (`gh`) ou GitLab (`glab`)
   - Créer le repo, push, fournir le one-liner d'installation
   - Proposer la création d'un registre d'outils d'équipe
   - Voir `references/team-sharing-guide.md`
5. **Mettre à jour** mémoires et documentation

## Ressources disponibles

### Prompts Meta-Prompting (5 Niveaux — V2)
| Fichier | Niveau | Usage |
|---------|--------|-------|
| `prompts/first-run-init.md` | 0 - First-Run | Orchestration initialisation auto |
| `prompts/level-1-analyzer.md` | 1 - Analyseur | Diagnostic + Clarity Principles (V2) |
| `prompts/level-2-architect.md` | 2 - Architecte | Conception technique + export planning (V2) |
| `prompts/level-3-generator.md` | 3 - Générateur | Production fichiers + staleness metadata (V2) |
| `prompts/level-4-validator.md` | 4 - Validateur | Quality Gate + Security + Staleness (V2) |
| `prompts/wizard-interactive.md` | Wizard | Mode interactif pas-à-pas (V2) |

### Outils et Scripts (V2 — scripts exécutables)
| Fichier | Type | Description |
|---------|------|-------------|
| `tools/scripts/validate-frontmatter.js` | Script | Validation YAML des frontmatter |
| `tools/scripts/generate-file-tree.js` | Script | Génère l'arborescence projet |
| `tools/scripts/security-scan.py` | Script V2 | Scan sécurité automatisé des livrables |
| `tools/scripts/staleness-check.py` | Script V2 | Détection obsolescence des outils |
| `tools/scripts/validate-kit.py` | Script V2 | Validation automatisée complète du kit |
| `tools/scripts/cross-platform-export.py` | Script V2 | Export cross-platform 14+ outils |
| `tools/scripts/team-registry.py` | Script V2 | Registre d'outils d'équipe |
| `tools/templates/agents-md-template.md` | Template | Template AGENTS.md racine |
| `tools/templates/rule-template.md` | Template | Template Rule avec frontmatter |
| `tools/templates/skill-template.md` | Template | Template SKILL.md complet |
| `tools/templates/workflow-template.md` | Template | Template Workflow |
| `tools/generators/project-scaffold.js` | Générateur | Scaffolding arborescence |
| `tools/validators/agents-schema.json` | Validateur | Schéma AGENTS.md |
| `tools/validators/rule-schema.json` | Validateur | Schéma Rule |
| `tools/validators/skill-schema.json` | Validateur | Schéma SKILL.md |

### Données et Configuration
| Fichier | Contenu |
|---------|---------|
| `data/config.json` | Configuration V2 du générateur |
| `data/schemas/input-schema.json` | Schéma validation inputs |
| `data/schemas/output-schema.json` | Schéma validation outputs |
| `data/stack-mappings.json` | Mapping stack → outils recommandés |
| `data/platform-mappings.json` | Mapping plateforme → formats export (V2) |

### Checklists Qualité
| Fichier | Moment |
|---------|--------|
| `checklists/pre-execution.md` | Avant exécution |
| `checklists/post-execution.md` | Après exécution |
| `checklists/quality-checks.md` | Vérification qualité globale |
| `checklists/premium-deliverables.md` | Checklist livrables premium |
| `checklists/security-checks.md` | Checklist sécurité (V2) |

### Références (V2)
| Fichier | Contenu |
|---------|---------|
| `references/documentation/windsurf-docs.md` | Documentation officielle |
| `references/articles/best-practices.md` | Best practices collectées |
| `references/standards/skill-standards.md` | Standards applicables |
| `references/cross-platform-guide.md` | Guide export multi-IDE (V2) |
| `references/team-sharing-guide.md` | Guide partage équipe (V2) |
| `references/security-guide.md` | Guide sécurité (V2) |
| `references/staleness-guide.md` | Guide détection obsolescence (V2) |

### Intégrations
| Fichier | Contenu |
|---------|---------|
| `integrations/mcp/servers.json` | Serveurs MCP configurables |
| `integrations/apis/generator-api-spec.yaml` | Spec API interne |

## Intégrations avec d'autres skills

- `@project-context-analyzer` → Contexte automatique (Phase 0)
- `@docs-auto-updater` → Synchronisation documentation (Phase 5)
- `@tools-documentation` → Guide utilisateur final
- `@specification-brainstorm` → Atelier cahier des charges (auto-init Phase 0b)
- `@debug-analyzer` → Diagnostic en cas d'erreur
- `@rag-knowledge-manager` → Configuration RAG post-génération
- `@mcp-connector` → Configuration MCP post-génération

## Navigation dans le skill

1. **Lancer** via `@premium-project-generator-v2` avec les variables projet
2. **Mode wizard** (optionnel) : ajouter `interactive_mode: true` pour guidage pas-à-pas
3. **Suivre** les 4 niveaux de meta-prompting séquentiellement
4. **Valider** avec Security Scan + Staleness Check intégrés
5. **Exporter** vers d'autres plateformes si nécessaire
6. **Partager** avec l'équipe en un clic
7. **Auditer** périodiquement avec les scripts de staleness

## Notes V2

Ce skill est conçu comme **produit premium V2**. Chaque livrable suit les
standards enterprise-grade et inclut les 10 améliorations :
- Security Scan + Staleness Check automatisés
- Export cross-platform (14+ IDEs)
- Partage équipe GitHub/GitLab intégré
- Discovery agressive (Clarity Principles)
- Scripts de validation exécutables
- Mode wizard interactif
- Registre d'outils d'équipe

**Tarification** : 2500€ (justifiée par V1 2000€ + 10 améliorations majeures).
