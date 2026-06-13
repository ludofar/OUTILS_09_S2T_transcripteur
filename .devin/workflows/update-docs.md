---
description: "Scanner et mettre à jour le guide utilisateur des outils Windsurf"
---

# /update-tools-docs

## Objectif
Régénérer le `TOOLS_USERGUIDE.md` après modification des outils Windsurf.

## Prérequis
- Outils Windsurf existants dans `.devin/`
- Skill `docs-auto-updater` initialisé (auto-en first-run)

## Étapes

### 1. Scan

**Commande** : `@docs-auto-updater`

Scanner l'arborescence `.devin/` :
- Extraire les frontmatter des Rules
- Extraire les structures des Skills
- Lister les Workflows
- Lire les configs MCP et RAG
- Vérifier la présence de README internes pour chaque skill

### 2. Diff

Le skill compare avec la version précédente du guide :
- Nouveaux outils ajoutés
- Outils modifiés
- Outils supprimés
- Documentation manquante

### 3. Preview

Le skill affiche un aperçu des changements :
- Nombre d'outils modifiés
- Sections impactées
- Score de couverture doc (0-100)
- Suggestions de mise à jour

### 4. Confirm

Le skill demande confirmation :
```
3 écarts détectés :
  - Rule : coding-standards-ts → non référencée dans AGENTS.md
  - Skill : payment-gateway → docs/README.md manquant
  - README projet → section .devin obsolète

Lancer /update-docs pour synchroniser ?
```

### 5. Generate & Sync

Le skill met à jour automatiquement :
- `AGENTS.md` avec les outils manquants
- `README.md` (section `.devin`)
- `TOOLS_USERGUIDE.md` avec index à jour
- `docs/README.md` interne de chaque skill

### 6. Suggestion commit

Le skill propose un message de commit :
```
docs: sync windsurf documentation
- Update AGENTS.md (3 outils ajoutés)
- Refresh TOOLS_USERGUIDE.md
- Add missing skill READMEs
```

## Checklist de sortie

- [ ] `TOOLS_USERGUIDE.md` régénéré
- [ ] Index à jour
- [ ] RAG et MCP inclus si applicable
- [ ] Diff documenté

## Liens

- Skill : `@docs-auto-updater`
- Output : `TOOLS_USERGUIDE.md`, `AGENTS.md` mis à jour
