# Checklist Post-Exécution - Premium Project Generator

## Validation des livrables générés

### AGENTS.md
- [ ] Fichier présent à la racine
- [ ] Structure hiérarchique (racine + modules)
- [ ] Rôle et contexte d'activation définis
- [ ] Liens Rules/Skills corrects

### Rules (minimum 4)
- [ ] `coding-standards.md` → frontmatter + contenu
- [ ] `domain-knowledge.md` → frontmatter + contenu
- [ ] `review-checklist.md` → frontmatter + contenu
- [ ] `security-guardrails.md` → frontmatter + contenu
- [ ] Toutes les Rules ≤ 12k caractères
- [ ] Triggers valides (always_on/glob/model_decision/manual)

### Skills (minimum 3)
- [ ] Chemin `.devin/skills/<kebab-name>/SKILL.md` correct
- [ ] Frontmatter YAML complet et valide
- [ ] Corps avec les 6 sections obligatoires
- [ ] Progressive disclosure respectée
- [ ] Dossiers utilisés cohérents

### Workflows (minimum 3)
- [ ] Invoquables via `/nom`
- [ ] Frontmatter avec description
- [ ] Étapes numérotées claires
- [ ] Skills et Rules référencés existent

### RAG
- [ ] `rag/config.yaml` généré si requis
- [ ] Sources locales indexables
- [ ] Requêtes prédéfinies testables

### MCP
- [ ] `integrations/mcp/servers.json` généré si requis
- [ ] Pas de secrets/tokens en clair
- [ ] Serveurs pertinents pour le stack

## Validation qualité premium

- [ ] Score de validation ≥ 85/100
- [ ] Chaque livrable a un exemple d'usage
- [ ] Documentation en Français
- [ ] Code/comments en Anglais
- [ ] TOOLS_USERGUIDE.md générable
- [ ] Checklist de validation rapide présente

## Sauvegarde et documentation

- [ ] `memories/context.md` mis à jour avec le nouveau projet
- [ ] `memories/preferences.md` sauvegardé
- [ ] `docs/README.md` documente le kit généré
- [ ] `docs/CHANGELOG.md` version initiale créée

## Métriques

| Métrique | Valeur |
|----------|--------|
| Nombre de Rules générées | ___ |
| Nombre de Skills générés | ___ |
| Nombre de Workflows générés | ___ |
| Score de validation | ___/100 |
| Temps de génération | ___ min |
