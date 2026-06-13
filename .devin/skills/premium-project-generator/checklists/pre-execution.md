# Checklist Pré-Exécution - Premium Project Generator

## Validation des inputs

- [ ] `project_name` défini et en kebab-case
- [ ] `tech_stack` précisé avec version si possible
- [ ] `business_domain` identifié
- [ ] `team_size` spécifié (solo/small/medium/large)
- [ ] `maturity` précisée (POC/MVP/production/legacy-migration)
- [ ] `constraints` listées si pertinent
- [ ] `languages` définies (défaut: fr)

## Prérequis système

- [ ] Windsurf IDE ouvert avec Cascade
- [ ] Droit d'écriture dans le workspace
- [ ] Node.js 18+ installé (si utilisation des scripts)
- [ ] Connexion internet (pour sources RAG distantes)

## Contexte utilisateur

- [ ] Aucune génération en cours sur le même projet
- [ ] `memories/context.md` sauvegardé si projet précédent
- [ ] Préférences utilisateur chargées depuis `memories/preferences.md`

## Configuration RAG

- [ ] `rag/config.yaml` accessible et valide
- [ ] Sources locales existent physiquement
- [ ] Espace disque suffisant pour l'indexation

## Configuration MCP

- [ ] `integrations/mcp/servers.json` valide
- [ ] Aucun token/secret en clair dans les configs
- [ ] Serveurs MCP pertinents pour le stack sélectionné

## Démarrage autorisé

> **ATTENTION** : Ne pas démarrer si un item critique (❌) est manquant.
> Les items optionnels (⚪) peuvent être complétés pendant l'exécution.

| Statut | Signification |
|--------|---------------|
| ✅ | Validé |
| ❌ | Bloquant - corriger avant de continuer |
| ⚪ | Optionnel - peut être ajouté plus tard |
