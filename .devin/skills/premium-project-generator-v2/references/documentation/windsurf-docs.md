# Documentation Windsurf — Références

## Sources officielles

- [Windsurf Documentation](https://docs.windsurf.com)
- [Windsurf Blog](https://windsurf.com/blog)

## Standards applicables

### AGENTS.md
- Fichier unique à la racine du projet
- Structure hiérarchique (racine → modules → sous-modules)
- Rôles, contexte d'activation, liens vers Rules et Skills

### Rules (.devin/rules/*.md)
- Frontmatter YAML obligatoire : name, description, trigger
- Triggers : always_on, glob, model_decision, manual
- Taille ≤ 12k caractères
- Kebab-case pour les noms de fichiers

### Skills (.devin/skills/<name>/SKILL.md)
- Structure en 14 dossiers possibles
- Frontmatter YAML complet pour l'invocation automatique
- Progressive disclosure pour optimiser le context window
- Corps avec sections : Vue d'ensemble, Cas d'usage, Procédure, Ressources

### Workflows (.devin/workflows/*.md)
- Invoquables via /nom dans le chat
- Frontmatter avec description
- Étapes numérotées claires

### RAG (rag/config.yaml)
- Sources locales et distantes
- Requêtes prédéfinies
- Boosting par type de fichier

### MCP (integrations/mcp/servers.json)
- Serveurs MCP configurables
- Tokens via variables d'environnement (jamais en clair)
