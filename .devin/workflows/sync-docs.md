---
description: Synchronise la documentation Windsurf et projet apres des modifications de skills, rules ou workflows
---

# Workflow : /sync-docs

## Commande
```
/sync-docs [scope]
```

**Arguments** :
- `scope` : `full` (defaut) | `windsurf-only` | `project-only` | `readme-only`

## Etapes

### 1. Scan
- `tools/scripts/scan-docs.js` parcourt `.devin/` et le projet
- Compare l'etat reel avec la documentation

### 2. Detection des ecarts
- Skills sans SKILL.md
- Workflows sans documentation
- Rules orphelines
- README desynchronise

### 3. Mise a jour proposee
- Generer un rapport Markdown des ecarts
- Proposer des correctifs ligne par ligne
- Appliquer sur validation utilisateur

### 4. Finalisation
- Mettre a jour `AGENTS.md` si agents modifies
- Mettre a jour `README.md` section `.devin`
- Generer `CHANGELOG.md` incremental

---

**Dependance** : `@docs-auto-updater`
