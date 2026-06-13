# Template Rule

## Usage
Copier ce template dans `.devin/rules/[nom-de-la-rule].md`

## Structure

```yaml
---
name: "{{RULE_NAME}}"
description: "{{RULE_DESCRIPTION}}"
trigger: "{{TRIGGER_MODE}}"
priority: {{PRIORITY}}
version: "{{VERSION}}"
---

# {{RULE_TITLE}}

## Règles principales

1. **Règle 1** : Description de la première règle
2. **Règle 2** : Description de la seconde règle
3. **Règle 3** : Description de la troisième règle

## Conventions

### Nommage
- {{CONVENTION_NAMING}}

### Structure
- {{CONVENTION_STRUCTURE}}

### Style
- {{CONVENTION_STYLE}}

## Anti-patterns

- ❌ Ne pas faire ceci
- ❌ Ne pas faire cela

## Exemples

### ✅ Correct
```{{LANG}}
{{EXAMPLE_GOOD}}
```

### ❌ Incorrect
```{{LANG}}
{{EXAMPLE_BAD}}
```

## Références

- [Lien vers documentation externe]
- `references/documentation/{{REF_FILE}}`
```

## Variables à remplacer
- `{{RULE_NAME}}` : Identifiant kebab-case
- `{{RULE_DESCRIPTION}}` : Description visible par Cascade
- `{{TRIGGER_MODE}}` : always_on | glob | model_decision | manual
- `{{PRIORITY}}` : high | medium | low
- `{{VERSION}}` : Semver
- `{{RULE_TITLE}}` : Titre lisible
- `{{CONVENTION_*}}` : Conventions spécifiques
- `{{LANG}}` : Langage de l'exemple
- `{{EXAMPLE_*}}` : Code d'exemple
