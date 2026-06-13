# Template Workflow

## Usage
Copier ce template dans `.devin/workflows/{{WORKFLOW_NAME}}.md`

## Structure

```markdown
---
description: "{{WORKFLOW_DESCRIPTION}}"
---

# {{WORKFLOW_TITLE}}

## Objectif

{{OBJECTIVE}}

## Prérequis

{{PREREQUISITES}}

## Étapes

### 1. {{STEP_1_TITLE}}

{{STEP_1_DESCRIPTION}}

**Commande** : `{{STEP_1_COMMAND}}`

**Output attendu** : {{STEP_1_OUTPUT}}

### 2. {{STEP_2_TITLE}}

{{STEP_2_DESCRIPTION}}

**Skill utilisé** : `@{{STEP_2_SKILL}}`

**Rule appliquée** : `{{STEP_2_RULE}}`

### 3. {{STEP_3_TITLE}}

{{STEP_3_DESCRIPTION}}

**Validation** : {{STEP_3_VALIDATION}}

## Checklist de sortie

- [ ] {{CHECKLIST_ITEM_1}}
- [ ] {{CHECKLIST_ITEM_2}}
- [ ] {{CHECKLIST_ITEM_3}}

## Troubleshooting

### Problème : {{PROBLEM_1}}
**Solution** : {{SOLUTION_1}}

### Problème : {{PROBLEM_2}}
**Solution** : {{SOLUTION_2}}

## Liens

- Skill principal : `@{{MAIN_SKILL}}`
- Documentation : `docs/{{DOC_FILE}}`
- RAG sources : `rag/{{RAG_FILE}}`
```

## Variables à remplacer
Toutes les variables entre `{{}}` doivent être personnalisées.
