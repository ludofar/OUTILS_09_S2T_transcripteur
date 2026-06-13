# Checklist Pré-Exécution V2 — Premium Project Generator

## Validation des inputs

- [ ] `project_name` défini et en kebab-case
- [ ] `tech_stack` précisé avec version si possible
- [ ] `business_domain` identifié
- [ ] `team_size` spécifié (solo/small/medium/large)
- [ ] `maturity` précisée (POC/MVP/production/legacy-migration)
- [ ] `constraints` listées si pertinent
- [ ] `languages` définies (défaut: fr)
- [ ] `export_platforms` définies si export demandé (V2)
- [ ] `team_sharing` spécifié si partage demandé (V2)
- [ ] `interactive_mode` activé si wizard souhaité (V2)

## Prérequis système

- [ ] Windsurf IDE ouvert avec Cascade
- [ ] Droit d'écriture dans le workspace
- [ ] Node.js 18+ installé (si utilisation des scripts JS)
- [ ] Python 3.8+ installé (security scan, staleness check, validation)
- [ ] Connexion internet (pour sources RAG distantes)
- [ ] `gh` ou `glab` authentifié (si team_sharing activé)

## Contexte utilisateur

- [ ] Aucune génération en cours sur le même projet
- [ ] `memories/context.md` sauvegardé si projet précédent
- [ ] Préférences utilisateur chargées depuis `memories/preferences.md`

## Configuration V2

- [ ] `data/config.json` à jour (version 2.0.0)
- [ ] `data/platform-mappings.json` accessible (si export)
- [ ] `data/stack-mappings.json` contient le stack du projet
- [ ] Scripts Python accessibles : security-scan.py, staleness-check.py, validate-kit.py

## Démarrage autorisé

| Statut | Signification |
|--------|---------------|
| ✅ | Validé |
| ❌ | Bloquant |
| ⚪ | Optionnel |
