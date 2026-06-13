# Checklist Qualité - Premium Project Generator

## Standards Windsurf

### Structure
- [ ] Noms de fichiers en kebab-case
- [ ] Chemins corrects (`.devin/skills/<name>/SKILL.md`)
- [ ] Pas de dossiers vides inutiles
- [ ] Arborescence cohérente avec le blueprint

### Frontmatter
- [ ] YAML syntaxiquement valide
- [ ] Champs obligatoires présents (name, description, version)
- [ ] Description suffisamment détaillée pour l'invocation auto
- [ ] Triggers cohérents avec l'usage
- [ ] Inputs/outputs documentés si applicable

### Progressive Disclosure
- [ ] `name` et `description` concis dans le prompt système
- [ ] Détails chargés uniquement à l'invocation
- [ ] Pas de contenu inutilement volumineux
- [ ] Références à des fichiers plutôt qu'inline si possible

## Qualité Premium (2000€)

### Cohérence
- [ ] Les skills référencent des rules qui existent
- [ ] Les workflows appellent des skills existants
- [ ] Les dépendances inter-skills sont résolues
- [ ] Les tags sont cohérents entre outils

### Documentation
- [ ] Exemples d'usage concrets dans chaque skill
- [ ] Navigation claire (README, TROUBLESHOOTING)
- [ ] Checklists présentes (pre/post/quality)
- [ ] CHANGELOG versionné

### Sécurité
- [ ] Pas de secrets/tokens en clair
- [ ] Variables d'environnement pour données sensibles
- [ ] Validation des inputs (JSON Schema)
- [ ] Pas d'exécution de code arbitraire

### Performance
- [ ] SKILL.md < 500 lignes idéalement
- [ ] Ressources chargées à la demande
- [ ] Mémoires utilisées efficacement
- [ ] Checklists courtes et actionnables

## Score qualité

| Catégorie | Poids | Score (0-20) |
|-----------|-------|-------------|
| Complétude livrables | 30% | ___ |
| Qualité frontmatter | 20% | ___ |
| Cohérence inter-fichiers | 20% | ___ |
| Exemples et doc | 15% | ___ |
| Standards premium | 15% | ___ |
| **TOTAL** | **100%** | **___/100** |

## Seuils

- **90-100** : Qualité exceptionnelle (premium+)
- **85-89** : Qualité premium acceptable (livraison autorisée)
- **70-84** : Qualité standard (patches recommandés)
- **< 70** : Refus livraison (rework obligatoire)
