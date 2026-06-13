---
name: "premium-style-rules"
description: "Règles de style et formatage pour les livrables premium"
trigger: "glob: '**/*.md'"
priority: medium
version: "1.0.0"
---

# Règles de Style - Premium Project Generator

## Markdown

### Titres
- H1 uniquement pour le titre principal du fichier
- H2 pour les sections principales
- H3 pour les sous-sections
- Jamais sauter un niveau (pas de H1 → H3)

### Listes
- Listes à puces pour les énumérations
- Listes numérotées pour les procédures séquentielles
- Cases à cocher pour les checklists

### Tables
- Utiliser des tables pour les comparaisons et mappings
- Alignement cohérent des colonnes
- En-têtes en gras

### Code
- Fenced blocks avec langage spécifié
- Inline code pour les noms de fichiers, variables, fonctions
- Pas de code dans les titres

## Langue

### Documentation
- **Français** obligatoire
- Termes techniques en Anglais conservés (ex: "progressive disclosure")
- Pas de traduction littérale des termes techniques

### Code
- **Anglais** obligatoire
- Variables, fonctions, classes en Anglais
- Comments en Anglais

## Progressive Disclosure

### SKILL.md
- `name` et `description` concis dans le prompt système
- Détails dans les fichiers annexes
- Références plutôt qu'inline pour le contenu volumineux

### Rules
- ≤ 12k caractères
- Frontmatter obligatoire
- Contenu actionnable
