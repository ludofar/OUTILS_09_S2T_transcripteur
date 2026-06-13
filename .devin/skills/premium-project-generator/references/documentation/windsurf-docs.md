# Documentation Officielle - Références Windsurf

## Skills
- **URL** : https://docs.windsurf.com/windsurf/cascade/skills
- **Description** : Documentation complète des skills Cascade
- **Sections clés** :
  - Création de skills (UI et manuel)
  - Format SKILL.md
  - Ajout de ressources support
  - Invocation automatique/manuelle
  - Scopes (workspace, global, system)

## Workflows
- **URL** : https://docs.windsurf.com/windsurf/cascade/workflows
- **Description** : Workflows pour tâches répétables
- **Différence avec Skills** : Workflows = manuels uniquement (/commande)

## Memories & Rules
- **URL** : https://docs.windsurf.com/windsurf/memories
- **Description** : Persistance du contexte et règles de comportement

## Knowledge Base (Beta)
- **URL** : https://docs.windsurf.com/windsurf/context-awareness
- **Description** : Indexation et recherche dans la codebase
- **Usage** : Base pour le système RAG du skill

## MCP (Model Context Protocol)
- **URL** : https://docs.windsurf.com/windsurf/mcp
- **Description** : Intégration de serveurs MCP
- **Config** : `~/.codeium/windsurf/mcp_config.json`

## Spécifications externes

### Agent Skills
- **URL** : https://agentskills.io/home
- **Description** : Spécification ouverte des skills
- **Référence** : Format standard inter-outils

### MCP Protocol
- **URL** : https://modelcontextprotocol.io/
- **Description** : Protocole d'intégration Model Context
- **Usage** : Connecteurs pour bases de données, APIs, fichiers

## Exemples communautaires

### Windsurf Agents (zenmindhacker)
- **URL** : https://github.com/zenmindhacker/windsurf-agents
- **Description** : Skills et workflows réels pour Windsurf
- **Skills** : Linear, Google Sync, Reporting, Figma, LangSmith

## Intégration dans le skill

Dans SKILL.md, référencer ces docs quand Cascade a besoin de contexte :

```markdown
## Références externes

Pour les détails sur la spécification, consulter :
- [Agent Skills Spec](https://agentskills.io/home)
- [Windsurf Skills Docs](https://docs.windsurf.com/windsurf/cascade/skills)

Pour les intégrations MCP :
- Voir `integrations/mcp/servers.json`
- [MCP Documentation](https://modelcontextprotocol.io/)
```

### Mise à jour
**Fréquence** : Vérifier mensuellement les changements de doc
**Responsable** : Maintien par l'auteur du skill
