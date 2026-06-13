---
name: premium-project-generator
description: |
  Skill PREMIUM pour générer automatiquement l'intégralité des outils Windsurf
  nécessaires à tout projet : AGENTS.md, Rules, Skills, Workflows, MCP, RAG.
  Utilise un meta-prompting hiérarchique à 4 niveaux (Analyseur → Architecte →
  Générateur → Validateur) pour produire des livrables production-ready.
  Adaptatif selon le stack, le domaine métier, la taille d'équipe et la maturité.
  
  Invoqué pour : création de projet, setup d'environnement, génération d'outils
  Windsurf premium, architecture de skills multi-étapes, configuration RAG/MCP.
version: 1.0.0
author: Architecte Système Windsurf Premium
tags:
  - premium
  - project-generator
  - meta-prompting
  - windsurf-tools
  - rag
  - mcp
  - automation
category: Architecture
scope: workspace
prerequisites:
  - Windsurf IDE avec Cascade
  - Connaissance basique du projet (stack, domaine, contraintes)
  - Droit d'écriture dans le workspace
  - Node.js 18+ (si scripts utilisés)
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
auto_invoke: false
confidence_threshold: 0.8
rag_sources: ["local", "remote"]
mcp_servers: ["filesystem"]
---

# Premium Project Generator

## Vue d'ensemble

Ce skill **PREMIUM** est le cœur du système d'outillage Windsurf. Il génère
automatiquement et intelligemment l'intégralité des outils nécessaires à tout
projet, quelle que soit sa taille ou sa complexité.

**Valeur unique** :
- **First-Run Auto-Init** : À sa première exécution dans un workspace, il déploie
  automatiquement les 3 skills de base fondamentaux :
  1. `@specification-brainstorm` — Atelier de cahier des charges interactif
  2. `@docs-auto-updater` — Synchronisation auto de la documentation Windsurf & projet
  3. Le **meta-prompting à 4 niveaux** (Analyseur → Architecte → Générateur → Validateur)
- **Meta-prompting à 4 niveaux** : Production des livrables principaux (Rules, Skills, Workflows)
- **Contexte auto-détecté** : Lecture du rapport `@project-context-analyzer` pour zéro friction

Ce skill est conçu comme **produit premium** (valeur 2000€). Chaque livrable
suit les standards enterprise-grade.

**Tarification de référence** : Ce système est conçu pour une valeur de 2000€,
justifiée par :
- L'automatisation complète du setup d'un projet
- La qualité enterprise-grade des livrables
- L'adaptation contextuelle (stack, domaine, équipe, maturité)
- L'intégration RAG et MCP native
- La maintenance auto-documentée

## Ce que fait ce skill à sa première lancée (First-Run)

Quand vous copiez ce skill dans un projet et que vous invoquez
`@premium-project-generator` pour la **toute première fois**, voici la séquence
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
- **Scripts** : `scan-docs.js`, `update-readme.js`
- **Workflow associé** : `/update-docs` (`.devin/workflows/update-tools-docs.md`)

#### C. **Meta-prompting à 4 niveaux** (Système principal)
- **Vérification** : Les 4 prompts existent déjà dans `prompts/level-*.md`
- **Workflow associé** : `/init-project` (`.devin/workflows/init-project.md`)
  qui orchestre : Analyseur → Architecte → Générateur → Validateur

### 3. Phase Discovery (Contexte auto-détecté)
- Le skill tente de lire `data/context-report.json` produit par
  `@project-context-analyzer` (si disponible)
- S'il est présent et que `confidence_score >= 80` : les inputs projet sont
  pré-remplis automatiquement (nom, stack, domaine, équipe, maturité)
- Sinon : 3 questions maximum à l'utilisateur

### 4. Lancement du meta-prompting principal
Une fois l'infrastructure initialisée et le contexte chargé, les 4 niveaux
s'exécutent séquentiellement :
1. **Analyseur** (Niveau 1) : Diagnostic et rapport d'analyse
2. **Architecte** (Niveau 2) : Blueprint technique des outils à générer
3. **Générateur** (Niveau 3) : Production concrète des fichiers (AGENTS.md, Rules, Skills, Workflows, RAG, MCP)
4. **Validateur** (Niveau 4) : Quality gate avec score global (minimum 85/100)

### 5. Finalisation et synchronisation
- Génération de `TOOLS_USERGUIDE.md`
- **Appel automatique** à `@docs-auto-updater` pour synchroniser la documentation
- Mise à jour des mémoires (`memories/context.md`, `memories/preferences.md`)

### Récapitulatif First-Run
Au total, après un premier `@premium-project-generator` dans un projet vierge,
le workspace contient :

| Élément | Quantité | Détail |
|---------|----------|--------|
| Skills fondamentaux | 3 | `specification-brainstorm`, `docs-auto-updater`, `premium-project-generator` |
| Workflows | 3 | `/init-project`, `/brainstorm`, `/update-docs` |
| Livrables générés | 10+ | AGENTS.md, 4+ Rules, 3+ Skills métier, 3+ Workflows, RAG, MCP |
| Documentation | 3 | TOOLS_USERGUIDE.md, README interne, memories |

**Temps estimé** : 5 minutes de setup, 30-40 minutes de génération auto-guidée.

## Cas d'usage

1. **Bootstrap projet (First-Run)** : Copier le skill dans un projet vierge →
   `@premium-project-generator` auto-initie les 3 skills de base → génère le
   kit complet sans configuration manuelle.
2. **Migration legacy** : Moderniser les outils d'un projet existant
3. **Scaling équipe** : Générer des rules et skills adaptés à une équipe croissante
4. **Audit & refonte** : Analyser et améliorer les outils existants
5. **Formation** : Servir d'exemple de référence pour l'architecture Windsurf premium

## Procédure pas à pas (Meta-Prompting 4 Niveaux)

### Phase 0 : Discovery (Cadrage)

**Automatique via @project-context-analyzer** :
1. **Vérifier** si `data/context-report.json` existe (produit par `@project-context-analyzer`)
2. **Si oui** :
   - **Charger** le rapport et extraire : `project_name`, `tech_stack`, `business_domain`, `team_size`, `maturity`, `constraints`, `languages`
   - **Si** `confidence_score >= 80` : utiliser directement ces valeurs, passer à la Phase 0b
   - **Si** `confidence_score < 80` : présenter les valeurs détectées à l'utilisateur pour validation rapide
3. **Si non** : exécuter `@project-context-analyzer` ou demander manuellement :
   - `project_name`, `tech_stack`, `business_domain`, `team_size`, `maturity`
   - Si ambiguïté : poser 3 questions ciblées maximum

### Phase 0b : First-Run Auto-Initialization (Skills de base)

**Objectif** : Si c'est la première exécution du générateur dans ce workspace,
déployer automatiquement les 3 skills fondamentaux avant de lancer le
meta-prompting principal.

**Détection du first-run** :
1. **Vérifier** si `.devin/skills/specification-brainstorm/SKILL.md` existe
2. **Vérifier** si `.devin/skills/docs-auto-updater/SKILL.md` existe
3. **Si l'un des deux est absent** → mode first-run activé

**Étapes d'initialisation (ordre strict)** :

#### Étape A : Système de Brainstorming
1. **Créer** `.devin/skills/specification-brainstorm/SKILL.md`
   - Template : `tools/templates/skill-template.md`
   - Contenu : atelier de cahier des charges interactif avec mémoire
   - Prompts : `prompts/brainstorm-system.md`, `prompts/brainstorm-questions.md`
   - Mémoire : `memories/last-brainstorm.md`
2. **Créer** `.devin/workflows/meta-brainstorm.md`
   - Workflow manuel `/brainstorm` pour lancer l'atelier
3. **Message utilisateur** : "Skill `specification-brainstorm` initialisé."

#### Étape B : Système de mise à jour documentation
1. **Créer** `.devin/skills/docs-auto-updater/SKILL.md`
   - Contenu : scan, détection d'écarts, mise à jour auto
   - Scripts : `tools/scripts/scan-docs.js`, `tools/scripts/update-readme.js`
   - Schéma : `data/sync-schema.json`
2. **Créer** `.devin/workflows/update-tools-docs.md`
   - Workflow manuel `/update-docs` pour synchroniser la doc
3. **Message utilisateur** : "Skill `docs-auto-updater` initialisé."

#### Étape C : Système de meta-prompting à 4 niveaux
1. **Vérifier** que les 4 prompts de meta-prompting existent :
   - `prompts/level-1-analyzer.md`
   - `prompts/level-2-architect.md`
   - `prompts/level-3-generator.md`
   - `prompts/level-4-validator.md`
2. **Si absent** : les générer à partir des templates internes
3. **Créer** `.devin/workflows/init-project.md`
   - Workflow manuel `/init-project` qui orchestre les 4 niveaux

**Output de la Phase 0b** :
- 2 nouveaux skills dans `.devin/skills/`
- 2 nouveaux workflows dans `.devin/workflows/`
- Le système de meta-prompting prêt à l'emploi
- Passage automatique à la Phase 1

### Phase 1 : ANALYSEUR (Niveau 1)

**Objectif** : Diagnostiquer le besoin et cartographier les zones d'ombre

1. **Charger** le prompt `prompts/level-1-analyzer.md`
2. **Analyser** les inputs du projet :
   - Stack technique → compatibilité avec l'écosystème Windsurf
   - Domaine métier → contraintes réglementaires et best practices
   - Taille équipe → complexité des outils (solo = simple, large = enterprise)
   - Maturité → POC (léger) vs production (robuste)
   - Contraintes → RGPD, accessibilité, i18n, performance
3. **Produire** `analysis_report.json` avec :
   - Besoins identifiés
   - Zones d'ombre à clarifier
   - Dépendances externes détectées
   - Risques anticipés
   - Recommandations préliminaires

**Output** : Fichier `data/analysis-report.json`

### Phase 2 : ARCHITECTE (Niveau 2)

**Objectif** : Transformer l'analyse en blueprint technique complet

1. **Charger** le prompt `prompts/level-2-architect.md`
2. **Concevoir** l'architecture d'outillage :
   - Quels livrables créer (AGENTS.md, Rules, Skills, Workflows)
   - Quels dossiers du skill activer (sur 14 disponibles)
   - Quelles librairies externes recommandées (`external/`)
   - Quelles sources RAG indexer (`rag/`)
   - Quels serveurs MCP configurer (`integrations/mcp/`)
   - Quelles références documenter (`references/`)
3. **Produire** `architecture_blueprint.json` avec :
   - Liste des livrables avec priorisation MVP first
   - Mapping stack → outils recommandés
   - Décisions d'architecture justifiées
   - Plan de déploiement séquentiel

**Output** : Fichier `data/architecture-blueprint.json`

### Phase 3 : GÉNÉRATEUR (Niveau 3)

**Objectif** : Produire tous les fichiers concrets

1. **Charger** le prompt `prompts/level-3-generator.md`
2. **Générer** dans l'ordre strict :
   - `/AGENTS.md` racine
   - `.devin/rules/*.md` (minimum 4 rules adaptatives)
   - `.devin/skills/*/SKILL.md` (skills métier + skills système)
   - `.devin/workflows/*.md` (workflows manuels)
   - `.devin/rag/config.yaml` (si RAG requis)
   - `.devin/integrations/mcp/servers.json` (si MCP requis)
3. **Utiliser** les templates de `tools/templates/` pour chaque type de fichier
4. **Valider** chaque fichier contre les schémas de `data/schemas/`

**Output** : Fichiers concrets dans l'arborescence du projet

### Phase 4 : VALIDATEUR (Niveau 4)

**Objectif** : Quality gate avant livraison

1. **Charger** le prompt `prompts/level-4-validator.md`
2. **Vérifier** :
   - Tous les frontmatter YAML sont valides
   - Les triggers sont cohérents avec le stack
   - Les dépendances inter-skills sont résolues
   - La progressive disclosure est respectée
   - Les schémas inputs/outputs sont complets
3. **Produire** `validation_report.json` avec :
   - Score de qualité global (0-100)
   - Liste des erreurs/correctifs
   - Patches à appliquer
   - Checklist de validation rapide

**Output** : Fichier `data/validation-report.json` + patches éventuels

### Phase 5 : Finalisation

1. **Générer** `TOOLS_USERGUIDE.md` via le skill `tools-documentation`
2. **Invoquer** `@docs-auto-updater` pour synchroniser :
   - `AGENTS.md` avec les nouveaux outils
   - `README.md` (section `.devin`)
   - `TOOLS_USERGUIDE.md` avec les skills/rules/workflows générés
   - Les `docs/README.md` internes de chaque skill
3. **Mettre à jour** `memories/context.md` avec le contexte du projet
4. **Sauvegarder** les préférences dans `memories/preferences.md`
5. **Documenter** dans `docs/README.md`

## Ressources disponibles

### Prompts Meta-Prompting (4 Niveaux)
| Fichier | Niveau | Usage |
|---------|--------|-------|
| `prompts/first-run-init.md` | 0 - First-Run | Orchestration de l'initialisation auto |
| `prompts/level-1-analyzer.md` | 1 - Analyseur | Diagnostic & cadrage |
| `prompts/level-2-architect.md` | 2 - Architecte | Conception technique |
| `prompts/level-3-generator.md` | 3 - Générateur | Production fichiers |
| `prompts/level-4-validator.md` | 4 - Validateur | Quality Gate |

### Outils et Scripts
| Fichier | Type | Description |
|---------|------|-------------|
| `tools/scripts/validate-frontmatter.js` | Script | Validation YAML des frontmatter |
| `tools/scripts/generate-file-tree.js` | Script | Génère l'arborescence projet |
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
| `data/config.json` | Configuration par défaut du générateur |
| `data/schemas/input-schema.json` | Schéma validation inputs |
| `data/schemas/output-schema.json` | Schéma validation outputs |
| `data/stack-mappings.json` | Mapping stack → outils recommandés |
| `data/domain-constraints.json` | Contraintes par domaine métier |

### Checklists Qualité
| Fichier | Moment |
|---------|--------|
| `checklists/pre-execution.md` | Avant exécution (variables, prérequis) |
| `checklists/post-execution.md` | Après exécution (fichiers, validation) |
| `checklists/quality-checks.md` | Vérification qualité globale |
| `checklists/premium-deliverables.md` | Checklist livrables 2000€ |

### Connaissances
| Fichier | Contenu |
|---------|---------|
| `knowledge/guidelines.md` | Principes architecturaux du générateur |
| `knowledge/conventions.md` | Conventions de codage et nommage |
| `knowledge/stack-compatibility.md` | Matrice de compatibilité stacks |
| `knowledge/pricing-justification.md` | Justification valeur 2000€ |

### Librairies Externes
| Fichier | Contenu |
|---------|---------|
| `external/repositories/github-sources.md` | Dépôts de référence |
| `external/packages/npm-references.json` | Packages recommandés |
| `external/libraries/vendor-libs.md` | Librairies tierces |

### Sources RAG
| Fichier | Contenu |
|---------|---------|
| `rag/config.yaml` | Configuration RAG du générateur |
| `rag/sources/index.md` | Index des sources de connaissances |
| `rag/queries/project-setup.yaml` | Requête prédéfinie setup projet |

### Intégrations
| Fichier | Contenu |
|---------|---------|
| `integrations/mcp/servers.json` | Serveurs MCP configurables |
| `integrations/apis/generator-api-spec.yaml` | Spec API interne |

### Références
| Fichier | Contenu |
|---------|---------|
| `references/documentation/windsurf-docs.md` | Documentation officielle |
| `references/articles/best-practices.md` | Best practices collectées |
| `references/standards/skill-standards.md` | Standards applicables |

## Intégrations

### Liens avec d'autres skills
- `@project-context-analyzer` → Fournit le contexte automatique avant génération (Phase 0)
- `@docs-auto-updater` → Synchronise la documentation après chaque génération (Phase 5)
- `@tools-documentation` → Génère le guide utilisateur final
- `@specification-brainstorm` → Atelier cahier des charges (auto-initié en Phase 0b)
- `@debug-analyzer` → Diagnostic en cas d'erreur génération
- `@rag-knowledge-manager` → Configuration RAG post-génération
- `@mcp-connector` → Configuration MCP post-génération

### Mémoires utilisées
- `memories/context.md` : Contexte du projet en cours
- `memories/preferences.md` : Préférences utilisateur (stack favori, style doc)
- `memories/history.md` : Historique des générations précédentes

### Règles appliquées
- `rules/coding-rules.md` : Conventions de code pour les scripts
- `rules/style-rules.md` : Style et formatage des livrables
- `rules/premium-rules.md` : Standards qualité premium

### Librairies externes
- `external/repositories/github-sources.md` : Dépôts patterns
- `external/packages/npm-references.json` : Outils de validation

### Sources RAG
- `rag/config.yaml` : Indexation des connaissances du générateur
- `rag/sources/index.md` : Documents métier indexés

### Intégrations MCP
- `integrations/mcp/servers.json` : Serveurs disponibles

### Références
- `references/documentation/windsurf-docs.md` : Docs officielles
- `references/standards/skill-standards.md` : Standards

## Navigation dans le skill

Pour utiliser ce skill efficacement :
1. **Lancer** via `@premium-project-generator` avec les variables projet
2. **Suivre** les 4 niveaux de meta-prompting séquentiellement
3. **Valider** chaque phase avec les checklists correspondantes
4. **Générer** les livrables dans l'ordre imposé
5. **Finaliser** avec le guide utilisateur auto-généré
6. **Explorer** `external/` pour les librairies recommandées
7. **Configurer** `rag/` et `integrations/` post-génération
8. **Lire** `references/` pour les standards et documentation

## Notes

Ce skill est conçu comme **produit premium**. Chaque livrable suit les
standards enterprise-grade et inclut :
- Frontmatter YAML complet et validé
- Documentation inline exhaustive
- Exemples d'usage concrets
- Tests de validation intégrés
- Checklist de qualité

**Tarification** : 2000€ (valeur justifiée par l'automatisation complète
du setup projet, la qualité enterprise-grade et le gain de temps estimé
à 40+ heures de travail manuel).
