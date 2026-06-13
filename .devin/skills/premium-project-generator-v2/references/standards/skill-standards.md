# Standards de Qualité — Skills Windsurf

## Structure obligatoire

Chaque skill doit résider dans `.devin/skills/<kebab-name>/SKILL.md`.

## Frontmatter YAML obligatoire

```yaml
---
name: kebab-case-name
description: |
  Description concise visible par Cascade pour l'invocation automatique.
version: 1.0.0
---
```

## Champs recommandés

- `author` : Auteur du skill
- `tags` : Mots-clés pour la découverte
- `category` : Catégorie fonctionnelle
- `scope` : workspace | global | system
- `prerequisites` : Prérequis système
- `dependencies` : Dépendances inter-skills
- `triggers` : Mots-clés d'activation
- `inputs` / `outputs` : Variables
- `auto_invoke` : Invocation automatique
- `confidence_threshold` : Seuil de confiance (0-1)

## V2 : Champs staleness

```yaml
metadata:
  created: YYYY-MM-DD
  last_reviewed: YYYY-MM-DD
  review_interval_days: 90
  generator: premium-project-generator-v2
  generator_version: 2.0.0
```

## Corps du SKILL.md

### Sections obligatoires
1. **Vue d'ensemble** — Ce que fait le skill
2. **Cas d'usage** — Quand l'utiliser
3. **Procédure pas à pas** — Comment l'utiliser
4. **Ressources disponibles** — Fichiers référencés
5. **Intégrations** — Liens avec d'autres skills
6. **Navigation** — Guide rapide d'utilisation

### Sections recommandées
- Exemples concrets (input → output)
- Troubleshooting
- Notes et limitations

## Conventions de nommage

- **Fichiers** : kebab-case (`my-skill-name`)
- **Dossiers** : kebab-case
- **Documentation** : Français
- **Code / comments** : Anglais
- **Variables** : camelCase (JS/TS) ou snake_case (Python)

## Limites

- Rule ≤ 12 000 caractères
- SKILL.md ≤ 500 lignes (recommandé)
- Description ≥ 10 caractères (pour l'auto-invocation)
