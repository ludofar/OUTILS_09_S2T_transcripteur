---
name: project-context-analyzer
description: |
  Skill d'analyse et de discovery qui scanne le workspace cible (.devin,
  README, fichiers de config, structure projet) pour extraire automatiquement
  le contexte nécessaire à @[premium-project-generator].
  
  Il produit un rapport de contexte structuré (data/context-report.json) et
  met à jour les mémoires (memories/context.md) pour que le générateur
  premium sache exactement dans quel projet et quel environnement il va
  travailler, sans poser de questions inutiles.
  
  Invoqué pour : préparer l'exécution de @premium-project-generator,
  auditor un projet existant, initialiser la mémoire d'un workspace.
version: 1.0.0
author: Architecte Système Devin Premium
tags:
  - discovery
  - context-analysis
  - project-scanner
  - memory-initializer
  - premium-preparation
category: Architecture
scope: workspace
prerequisites:
  - Devin IDE avec Cascade
  - Droit de lecture sur l'ensemble du workspace
  - Node.js 18+ (pour le script de scan)
dependencies:
  - premium-project-generator
triggers:
  - analyze project context
  - discover workspace
  - scan project
  - prepare context
  - initialize memory
  - context report
  - before generate tools
inputs:
  workspace_path:
    type: string
    required: false
    default: "."
    description: "Chemin racine du workspace à analyser"
  output_path:
    type: string
    required: false
    default: ".devin/skills/premium-project-generator/data/context-report.json"
    description: "Chemin de sortie du rapport de contexte"
  deep_scan:
    type: boolean
    required: false
    default: true
    description: "Activer l'analyse profonde (package.json, deps, config files)"
outputs:
  context_report:
    type: object
    description: "Rapport de contexte structuré avec tous les éléments détectés"
  memory_update:
    type: string
    description: "Mise à jour de memories/context.md du générateur"
  detected_stack:
    type: string
    description: "Stack technique déduite"
  detected_domain:
    type: string
    description: "Domaine métier déduit"
  confidence_score:
    type: number
    description: "Score de confiance global de l'analyse (0-100)"
auto_invoke: false
confidence_threshold: 0.75
rag_sources: ["local"]
mcp_servers: ["filesystem"]
---

# Project Context Analyzer

## Vue d'ensemble

Ce skill est le **préambule obligatoire** de @premium-project-generator. Il réalise
un scan complet du workspace cible pour extraire automatiquement :

- **Le contexte projet** : nom, stack, domaine, maturité, taille d'équipe
- **L'existant Devin** : rules, skills, workflows déjà présents
- **Les contraintes** : dépendances, normes, languages détectés
- **La documentation** : README, CONTRIBUTING, docs existantes

**Valeur unique** : Au lieu de demander à l'utilisateur de remplir manuellement
les inputs du générateur, ce skill les infère à 80%+ d'exactitude en quelques
secondes. Il élimine la friction de la Phase 0 (Discovery) du meta-prompting.

## Cas d'usage

1. **Bootstrap automatique** : Copier `premium-project-generator` dans un projet
   → lancer `@project-context-analyzer` → il remplit automatiquement la mémoire
   du générateur avec le contexte détecté.

2. **Audit pré-génération** : Avant de régénérer les outils Devin d'un projet
   existant, scanner pour comprendre ce qui est déjà en place et éviter les
   collisions.

3. **Migration legacy** : Analyser un projet ancien sans documentation pour en
   extraire la stack cachée (dépendances, frameworks, patterns).

4. **Multi-projet** : Travailler dans un mono-repo ? Ce skill produit un rapport
   par sous-projet détecté.

## Procédure pas à pas

### Phase 1 : Scan initial (Arborescence & Fichiers clés)

1. **Lister** la racine du workspace (`workspace_path`)
2. **Identifier** les fichiers de configuration clés :
   - `package.json` / `Cargo.toml` / `pyproject.toml` / `composer.json` / `go.mod`
   - `README.md` / `readme.md`
   - `.devin/` (si déjà existant)
   - Fichiers Docker / CI (`.github/`, `Dockerfile`)
3. **Extraire** le nom du projet depuis le dossier racine ou package.json

### Phase 2 : Analyse technique (Stack detection)

1. **Parser** le fichier de manifeste principal (package.json, etc.)
2. **Détecter** le framework frontend (React, Vue, Svelte, Angular, Next.js...)
3. **Détecter** le backend / runtime (Node, Python, Rust, Go, PHP...)
4. **Détecter** la base de données (PostgreSQL, MongoDB, MySQL, Prisma...)
5. **Détecter** les outils de build (Vite, Webpack, Turborepo, Nx...)
6. **Détecter** les services externes (Stripe, Firebase, AWS, Auth0...)
7. **Construire** la string `tech_stack` formatée pour le générateur

### Phase 3 : Analyse métier (Domain detection)

1. **Lire** le README.md (titre, description, premières lignes)
2. **Rechercher** les mots-clés métier :
   - fintech : paiement, banque, trading, crypto, finance
   - health : santé, patient, médical, clinique, DMP
   - ecommerce : shop, boutique, panier, produit, commande
   - education : cours, élève, professeur, MOOC, formation
   - iot : capteur, device, embarqué, raspberry, arduino
   - devops : CI/CD, infra, terraform, kubernetes, deploy
   - saas : subscription, tenant, B2B, dashboard
   - social : chat, message, communauté, forum, réseau
3. **Mapper** sur l'enum `business_domain` du générateur
4. **Détecter** les langues utilisées (i18n files, lang attributes)

### Phase 4 : Analyse de l'existant Devin

1. **Lister** `.devin/rules/*.md` → compter et résumer
2. **Lister** `.devin/skills/*/` → compter et lister les noms
3. **Lister** `.devin/workflows/*.md` → compter
4. **Détecter** RAG existant (`.devin/rag/`)
5. **Détecter** MCP existant (`.devin/integrations/mcp/`)
6. **Évaluer** la maturité de l'outillage :
   - 0 outil → POC / MVP
   - 1-3 rules → MVP
   - 4+ rules + skills → production
   - Vieux outils mal structurés → legacy-migration

### Phase 5 : Déduction de la taille d'équipe

1. **Signaux "solo"** : pas de CONTRIBUTING, auteur unique dans git, petit scope
2. **Signaux "small"** : 2-5 contributeurs git, scope moyen
3. **Signaux "medium"** : 6-15 contributeurs, mono-repo ou plusieurs services
4. **Signaux "large"** : 15+, documentation extensive, multi-équipes

### Phase 6 : Détection des contraintes

1. **RGPD** : mentions "données personnelles", "cookie", "consent", "GDPR"
2. **Sécurité** : auth, oauth, jwt, bcrypt, helmet, CSP
3. **Accessibilité** : a11y, aria, wcag, screen reader
4. **i18n** : react-intl, i18next, next-intl, lang/
5. **Performance** : lighthouse, bundle analyzer, caching, CDN
6. **Tests** : jest, cypress, playwright, vitest, coverage

### Phase 7 : Production du rapport

1. **Assembler** `data/context-report.json` conforme au schéma
2. **Calculer** le `confidence_score` (moyenne pondérée des détections)
3. **Mettre à jour** `memories/context.md` du générateur avec les valeurs détectées
4. **Produire** un résumé lisible pour l'utilisateur

## Ressources disponibles

### Prompts
| Fichier | Usage |
|---------|-------|
| `prompts/discovery-prompt.md` | Instructions LLM pour l'analyse textuelle (README, docs) |

### Outils et Scripts
| Fichier | Type | Description |
|---------|------|-------------|
| `tools/scripts/scan-workspace.js` | Script | Scan automatique du filesystem et extraction de données brutes |
| `data/context-output-schema.json` | Schéma | Validation du rapport de contexte produit |

### Données
| Fichier | Contenu |
|---------|---------|
| `data/stack-keywords.json` | Mapping mots-clés → frameworks/stacks |
| `data/domain-keywords.json` | Mapping mots-clés → domaines métiers |
| `data/maturity-indicators.json` | Indicateurs de maturité par stack |

### Exemples
| Fichier | Contenu |
|---------|---------|
| `examples/sample-output.json` | Exemple de rapport produit sur un projet Next.js e-commerce |

## Intégrations

### Liens avec d'autres skills
- `@premium-project-generator` → Client principal : consomme le context-report.json
- `@tools-documentation` → Peut être appelé après pour documenter l'existant

### Mémoires utilisées
- `memories/context.md` : Écrit le contexte détecté pour le générateur
- `memories/preferences.md` : Lit les préférences utilisateur si elles existent

### Librairies externes
- Node.js `fs`, `path`, `child_process` (git log)

## Navigation dans le skill

Pour utiliser ce skill efficacement :
1. **Copier** `premium-project-generator` dans le workspace cible
2. **Lancer** `@project-context-analyzer` depuis le workspace cible
3. **Vérifier** le rapport produit et corriger les inférences si besoin
4. **Lancer** `@premium-project-generator` → il lira automatiquement le contexte

## Notes

- Le skill **ne modifie jamais** le code source du projet cible, il lit seulement.
- Si aucun `package.json` n'est trouvé, le skill se base sur les extensions de
  fichiers et la structure des dossiers.
- Le `confidence_score` indique la fiabilité : si < 60, l'utilisateur doit
  valider manuellement les inputs avant de lancer le générateur.
- Ce skill est conçu pour être **auto-suffisant** : il n'a pas besoin d'inputs
  manuels pour fonctionner, mais il accepte des corrections.
