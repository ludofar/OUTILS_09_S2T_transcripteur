# Index des Sources RAG - Premium Project Generator

## Sources locales

### knowledge/
- `guidelines.md` → Principes architecturaux du générateur
- `conventions.md` → Conventions de codage et nommage
- `stack-compatibility.md` → Matrice de compatibilité stacks
- `pricing-justification.md` → Justification valeur 2000€

### tools/templates/
- `agents-md-template.md` → Template AGENTS.md
- `rule-template.md` → Template Rule
- `skill-template.md` → Template SKILL.md complet
- `workflow-template.md` → Template Workflow

### tools/validators/
- `skill-schema.json` → Schéma validation SKILL.md frontmatter

### data/
- `config.json` → Configuration par défaut
- `stack-mappings.json` → Mapping stack → outils recommandés

### examples/
- `basic-usage.md` → Cas d'usage Next.js
- `input-examples/sample-input.json` → Input ecommerce
- `output-examples/sample-output.json` → Output validation

### docs/
- `README.md` → Documentation skill
- `CHANGELOG.md` → Historique versions
- `TROUBLESHOOTING.md` → Guide dépannage

## Sources distantes

### Documentation Windsurf
- **URL** : https://docs.windsurf.com/windsurf/cascade/skills
- **Type** : Documentation officielle
- **Pertinence** : Référence absolue pour le format SKILL.md

### Agent Skills Spec
- **URL** : https://agentskills.io/home
- **Type** : Spécification ouverte
- **Pertinence** : Format standard inter-outils

### MCP Documentation
- **URL** : https://modelcontextprotocol.io/
- **Type** : Protocole d'intégration
- **Pertinence** : Configuration des serveurs MCP

### Windsurf Knowledge Base
- **URL** : https://docs.windsurf.com/windsurf/context-awareness
- **Type** : Beta feature
- **Pertinence** : Indexation et recherche sémantique

## Mise à jour des sources

**Fréquence** : Vérifier mensuellement les sources distantes
**Responsable** : Maintien par l'utilisateur du skill
**Procédure** : Mettre à jour `rag/config.yaml` puis réindexer
