# Checklist Qualité V2 — Premium Project Generator

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
- [ ] **Métadonnées staleness V2 présentes** (created, last_reviewed, review_interval_days)

### Progressive Disclosure
- [ ] `name` et `description` concis dans le prompt système
- [ ] Détails chargés uniquement à l'invocation
- [ ] Pas de contenu inutilement volumineux
- [ ] Références à des fichiers plutôt qu'inline si possible

## Qualité Premium V2 (2500€)

### Cohérence
- [ ] Les skills référencent des rules qui existent
- [ ] Les workflows appellent des skills existants
- [ ] Les dépendances inter-skills sont résolues
- [ ] Les tags sont cohérents entre outils

### Documentation
- [ ] Exemples d'usage concrets dans chaque skill
- [ ] Navigation claire (README, TROUBLESHOOTING)
- [ ] Checklists présentes (pre/post/quality/security)
- [ ] CHANGELOG versionné

### Sécurité (V2)
- [ ] Security scan passé (score ≥ 7/10)
- [ ] Pas de secrets/tokens en clair
- [ ] Variables d'environnement pour données sensibles
- [ ] Validation des inputs (JSON Schema)

### Staleness (V2)
- [ ] Métadonnées de review dans chaque fichier
- [ ] Intervalles adaptés à la maturité
- [ ] Dépendances externes déclarées si applicable
- [ ] Schema expectations si APIs utilisées

### Cross-Platform (V2)
- [ ] Export testé sur au moins 1 plateforme Tier 2
- [ ] install.sh fonctionnel
- [ ] Instructions d'installation par plateforme dans README

### Partage Équipe (V2)
- [ ] Repo créable automatiquement (gh/glab)
- [ ] One-liner d'installation clair
- [ ] README avec instructions d'onboarding

## Score qualité V2

| Catégorie | Poids | Score |
|-----------|-------|-------|
| Complétude livrables | 25 | ___/25 |
| Qualité frontmatter | 15 | ___/15 |
| Cohérence inter-fichiers | 15 | ___/15 |
| Exemples et doc | 15 | ___/15 |
| Standards premium | 10 | ___/10 |
| **Security Score** (V2) | **10** | ___/10 |
| **Staleness Score** (V2) | **10** | ___/10 |
| **TOTAL** | **100** | **___/100** |

## Seuils

- **90-100** : Qualité exceptionnelle (premium+)
- **85-89** : Qualité premium acceptable (livraison autorisée)
- **70-84** : Qualité standard (patches recommandés)
- **< 70** : Refus livraison (rework obligatoire)

## Commande de validation automatisée

```bash
python3 tools/scripts/validate-kit.py /path/to/kit --verbose
```
