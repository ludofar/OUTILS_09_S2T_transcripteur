# Template SKILL.md Complet

## Usage
Copier ce template dans `.devin/skills/{{SKILL_NAME}}/SKILL.md`

## Structure du dossier (14 dossiers types obligatoires)

Lors de la création d'un nouveau skill, créer l'arborescence complète suivante (même si certains dossiers restent vides initialement) :

```
.devin/skills/{{SKILL_NAME}}/
├── SKILL.md
├── tools/
│   ├── scripts/
│   ├── templates/
│   ├── generators/
│   └── validators/
├── prompts/
├── examples/
│   ├── input-examples/
│   └── output-examples/
├── knowledge/
│   └── references/
├── data/
│   ├── schemas/
│   ├── mappings/
│   └── fixtures/
├── checklists/
├── memories/
├── rules/
├── external/
│   ├── libraries/
│   ├── repositories/
│   └── packages/
├── rag/
│   ├── sources/
│   └── queries/
├── integrations/
│   ├── mcp/
│   └── apis/
├── references/
│   ├── documentation/
│   ├── articles/
│   └── standards/
├── workflows/
├── tests/
│   └── scenarios/
└── docs/
    ├── README.md
    ├── CHANGELOG.md
    ├── ARCHITECTURE.md
    └── TROUBLESHOOTING.md
```

## Structure

```yaml
---
name: {{SKILL_NAME}}
description: |
  {{SKILL_DESCRIPTION}}
  Visible par Cascade pour l'invocation automatique.
version: {{VERSION}}
author: {{AUTHOR}}
tags:
  {{TAGS}}
category: {{CATEGORY}}
scope: {{SCOPE}}
prerequisites:
  {{PREREQUISITES}}
dependencies:
  {{DEPENDENCIES}}
triggers:
  {{TRIGGERS}}
inputs:
  {{INPUTS}}
outputs:
  {{OUTPUTS}}
auto_invoke: {{AUTO_INVOKE}}
confidence_threshold: {{CONFIDENCE}}
rag_sources: {{RAG_SOURCES}}
mcp_servers: {{MCP_SERVERS}}
---

# {{SKILL_TITLE}}

## Vue d'ensemble

{{OVERVIEW}}

## Cas d'usage

1. **Cas 1** : {{USE_CASE_1}}
2. **Cas 2** : {{USE_CASE_2}}
3. **Cas 3** : {{USE_CASE_3}}

## Procédure pas à pas

### Phase 1 : Initialisation

1. Charger la configuration depuis `data/config.json`
2. Vérifier les prérequis avec `checklists/pre-execution.md`
3. Récupérer le contexte depuis `memories/context.md`

### Phase 2 : Analyse

1. Utiliser le prompt `prompts/analysis-prompt.md`
2. Valider les entrées contre `data/schemas/input-schema.json`
3. Consulter `knowledge/guidelines.md` pour les contraintes

### Phase 3 : Exécution

1. Appliquer le template approprié depuis `tools/templates/`
2. Exécuter les scripts dans `tools/scripts/` si nécessaire
3. Générer avec `tools/generators/` pour le scaffolding

### Phase 4 : Validation

1. Vérifier les sorties contre `data/schemas/output-schema.json`
2. Suivre `checklists/post-execution.md`
3. Valider avec les règles dans `rules/`

### Phase 5 : Finalisation

1. Mettre à jour `memories/context.md`
2. Sauvegarder les préférences dans `memories/preferences.md`
3. Documenter les résultats

## Ressources disponibles

### Outils et scripts
| Fichier | Description |
|---------|-------------|
| `tools/scripts/{{SCRIPT}}` | {{SCRIPT_DESC}} |
| `tools/templates/{{TEMPLATE}}` | {{TEMPLATE_DESC}} |
| `tools/validators/{{VALIDATOR}}` | {{VALIDATOR_DESC}} |
| `tools/generators/{{GENERATOR}}` | {{GENERATOR_DESC}} |

### Prompts et instructions
| Fichier | Usage |
|---------|-------|
| `prompts/system-prompt.md` | Instructions système |
| `prompts/analysis-prompt.md` | Phase d'analyse |
| `prompts/generation-prompt.md` | Phase de génération |

### Checklists
| Fichier | Moment |
|---------|--------|
| `checklists/pre-execution.md` | Avant exécution |
| `checklists/post-execution.md` | Après exécution |
| `checklists/quality-checks.md` | Vérification qualité |

## Intégrations

### Liens avec d'autres skills
{{SKILL_LINKS}}

### Mémoires utilisées
{{MEMORIES}}

### Règles appliquées
{{RULES}}

### Librairies externes
{{EXTERNAL_LIBS}}

### Sources RAG
{{RAG_SOURCES_DETAIL}}

### Intégrations MCP
{{MCP_DETAIL}}

### Références
{{REFERENCES}}

## Navigation dans le skill

Pour utiliser ce skill efficacement :
1. Lire `docs/README.md` pour la documentation complète
2. Consulter `examples/` pour comprendre les cas d'usage
3. Suivre les checklists pour la qualité
4. Vérifier `docs/TROUBLESHOOTING.md` en cas de problème

## Notes

{{NOTES}}
```

## Variables à remplacer
Toutes les variables entre `{{}}` doivent être personnalisées selon le projet.
