# Conventions de Codage - Premium Project Generator

## Nommage

### Fichiers et dossiers
- **Kebab-case** obligatoire : `premium-project-generator`, `coding-standards.md`
- **Extensions** : `.md` pour doc, `.js`/`.ts` pour code, `.json` pour config, `.yaml` pour data
- **Pas d'espaces** dans les noms de fichiers

### Identifiants
- **Skills** : `kebab-case`, minuscules, chiffres, tirets
  - ✅ `project-scaffold`, `debug-analyzer`
  - ❌ `projectScaffold`, `debug_analyzer`
- **Rules** : `kebab-case.md`
  - ✅ `coding-standards.md`
  - ❌ `codingStandards.md`, `coding_standards.md`
- **Workflows** : `kebab-case.md`, invoqués via `/nom`
  - ✅ `/init-project`, `/meta-brainstorm`

## Structure YAML

### Frontmatter
```yaml
---
name: "nom-du-skill"
description: |
  Description multi-lignes
  pour Cascade.
version: "1.0.0"
---
```

### Règles YAML
- 2 espaces d'indentation
- Pas de tabs
- Guillemets autour des chaînes contenant des caractères spéciaux
- Pipes `|` pour les descriptions multi-lignes

## Code

### Langue
- **Documentation** : Français
- **Code et comments** : Anglais
- **Variables** : Anglais

### JavaScript/Node.js
- ES modules (`import`/`export`) préférés
- `const` par défaut, `let` si mutation nécessaire
- Fonctions nommées pour la stack trace
- JSDoc pour les params et return types

### Scripts shell
- `set -euo pipefail` (fail fast)
- Couleurs : rouge erreur, vert succès, jaune warning
- Logging avec niveaux : INFO, WARN, ERROR

## Documentation

### Markdown
- H2 pour les sections principales
- H3 pour les sous-sections
- Listes à puces préférées aux paragraphes denses
- Fenced blocks avec langage
- Tables pour les comparaisons

### Exemples
Chaque livrable doit inclure :
- Un exemple d'input
- L'output attendu
- La commande d'activation

## Versioning

- **Semver** : `MAJOR.MINOR.PATCH`
- `MAJOR` : Changement incompatible
- `MINOR` : Nouvelle fonctionnalité
- `PATCH` : Correctif
- Documenter dans `CHANGELOG.md`
