---
name: docs-auto-updater
description: |
  Skill de maintenance et synchronisation automatique de la documentation
  Windsurf (.devin/docs) et projet (README, CONTRIBUTING, docs/).
  
  Analyse les changements de code, les nouveaux skills/rules/workflows générés
  et met à jour la documentation associée pour garantir qu'elle reste toujours
  synchronisée avec l'état réel du projet.
  
  Invoqué pour : mise à jour post-génération, synchronisation après refactoring,
  génération de changelogs, maintenance de la documentation.
version: 1.0.0
author: Architecte Système Windsurf Premium
tags:
  - documentation
  - sync
  - maintenance
  - auto-update
  - windsurf-tools
category: Maintenance
scope: workspace
prerequisites:
  - Windsurf IDE avec Cascade
  - Droit de lecture/écriture dans le workspace
  - Git initialisé (pour diff et changelogs)
dependencies:
  - premium-project-generator
triggers:
  - update documentation
  - sync docs
  - refresh readme
  - update windsurf docs
  - generate changelog
  - maintain docs
  - docs out of date
inputs:
  scan_scope:
    type: string
    required: false
    default: "full"
    enum: ["full", "windsurf-only", "project-only", "readme-only"]
    description: "Portée de la mise à jour"
  auto_commit:
    type: boolean
    required: false
    default: false
    description: "Créer un commit git avec les changements"
outputs:
  updated_files:
    type: array
    description: "Liste des fichiers mis à jour"
  changelog:
    type: string
    description: "Résumé des changements détectés et appliqués"
  sync_report:
    type: object
    description: "Rapport de synchronisation avec statistiques"
auto_invoke: false
confidence_threshold: 0.7
rag_sources: ["local"]
mcp_servers: ["filesystem"]
---

# Docs Auto-Updater

## Vue d'ensemble

Ce skill est le **gardien de la documentation**. Il garantit que la documentation
Windsurf et la documentation projet restent **toujours synchrones** avec le code
et les outils générés.

**Valeur unique** : Après une génération par `@premium-project-generator`, la
documentation est souvent obsolète dès qu'un skill est modifié. Ce skill détecte
automatiquement les écarts et les corrige.

## Cas d'usage

1. **Post-génération** : Après `@premium-project-generator`, synchroniser la
   documentation pour refléter les nouveaux outils créés.
2. **Refactoring** : Un skill a été renommé ? Les rules ont changé ? Mettre à
   jour TOOLS_USERGUIDE.md et le README automatiquement.
3. **Changelog** : Générer un CHANGELOG.md basé sur les commits et les fichiers
   `.devin` modifiés.
4. **Audit doc** : Vérifier que chaque skill a un README dans `docs/`, que
   chaque rule est référencée dans AGENTS.md.

## Procédure pas à pas

### Phase 1 : Scan de l'état actuel

1. **Lister** tous les fichiers `.devin/skills/*/SKILL.md`
2. **Lister** tous les fichiers `.devin/rules/*.md`
3. **Lister** tous les fichiers `.devin/workflows/*.md`
4. **Lire** le `README.md` racine
5. **Lire** le `TOOLS_USERGUIDE.md` s'il existe
6. **Lire** le `AGENTS.md` racine

### Phase 2 : Détection des écarts

Pour chaque skill détecté :
- Vérifier s'il est référencé dans `AGENTS.md`
- Vérifier s'il a une section dans `TOOLS_USERGUIDE.md`
- Vérifier s'il a un `docs/README.md` interne

Pour chaque rule détectée :
- Vérifier s'il y a une description dans `AGENTS.md`
- Vérifier si les triggers sont documentés

Pour chaque workflow détecté :
- Vérifier s'il est référencé dans le guide utilisateur

### Phase 3 : Mise à jour

1. **Mettre à jour** `AGENTS.md` avec les skills/rules/workflows manquants
2. **Mettre à jour** `TOOLS_USERGUIDE.md` avec les nouveaux outils
3. **Mettre à jour** `README.md` (section `.devin` si présente)
4. **Générer** ou mettre à jour `docs/README.md` pour chaque skill
5. **Mettre à jour** `memories/context.md` avec la date de dernière sync

### Phase 4 : Rapport

Produire `data/sync-report.json` avec :
- Fichiers mis à jour
- Écarts détectés mais non corrigés (avec raison)
- Score de couverture doc (0-100)
- Recommandations

## Ressources disponibles

### Scripts
| Fichier | Description |
|---------|-------------|
| `tools/scripts/scan-docs.js` | Scan la documentation existante |
| `tools/scripts/update-readme.js` | Met à jour le README avec les infos .devin |
| `tools/scripts/generate-changelog.js` | Génère un changelog depuis les commits git |

### Templates
| Fichier | Description |
|---------|-------------|
| `tools/templates/skill-readme-template.md` | Template README interne d'un skill |
| `tools/templates/tools-guide-section.md` | Template section TOOLS_USERGUIDE.md |

### Données
| Fichier | Contenu |
|---------|---------|
| `data/sync-schema.json` | Schéma du rapport de synchronisation |

## Intégrations

### Liens avec d'autres skills
- `@premium-project-generator` → Appelé automatiquement en Phase 5 (Finalisation)
- `@project-context-analyzer` → Lit le contexte pour personnaliser la doc

### Mémoires utilisées
- `memories/last-sync.md` : Date et contenu de la dernière synchronisation

## Navigation

1. **Invoquer** via `@docs-auto-updater`
2. **Choisir** le scope (`full`, `windsurf-only`, `project-only`)
3. **Vérifier** le rapport de sync
4. **Valider** les changements proposés

## Notes

- Ce skill ne supprime jamais de documentation sans confirmation
- Il préserve les sections manuelles ajoutées par l'utilisateur
- Le score de couverture doc vise 100% : chaque outil doit être documenté
