---
description: Point d'entree unique pour configurer un projet Windsurf complet — du contexte au kit final en un seul workflow
---

# Workflow : /setup-windsurf-tools

## Commande
```
/setup-windsurf-tools
```

**Usage** : Lancez ce workflow dans un projet vierge ou existant pour generer
le kit complet d'outils Windsurf avec la version premium V2.

## Etapes

### Phase 0 — Contexte (`/analyze-context`)
1. `@project-context-analyzer` scanne le workspace
2. Produit `data/context-report.json`
3. Si confidence < 80 : poser 3 questions a l'utilisateur

### Phase 1 — Generation (`/init-project-v2`)
1. `@premium-project-generator-v2` lance le meta-prompting 4 niveaux
2. `security-scan.py` verifie les livrables
3. `validate-kit.py` attribue un score 0-100
4. Si score < 70 : boucle de correction automatique

### Phase 2 — Export (optionnel)
1. Proposer l'export cross-platform (`/export-tools`)
2. Publier sur le registre equipe (`team-registry.py`)

### Phase 3 — Documentation (`/sync-docs` + `/generate-userguide`)
1. `@docs-auto-updater` synchronise README, AGENTS.md, CHANGELOG
2. `@windsurf-userguide-generator` genere :
   - `.devin/USERGUIDE.html` — Dashboard principal
   - `.devin/SKILLS-NETWORK.html` — Graphe relationnel interactif

### Phase 4 — Validation finale
1. Afficher le score global du kit
2. Lister les commandes disponibles (`/`, `@`)
3. Pointer vers `USERGUIDE.html` pour la navigation visuelle

## Livrables finaux

| Fichier | Description |
|---------|-------------|
| `AGENTS.md` | Agents hierarchiques |
| `.devin/rules/*.md` | 4+ rules adaptatives |
| `.devin/skills/*/SKILL.md` | Skills metier + systeme |
| `.devin/workflows/*.md` | Workflows operationnels |
| `.devin/rag/config.yaml` | Configuration RAG |
| `.devin/integrations/mcp/servers.json` | MCP servers |
| `.devin/USERGUIDE.html` | Dashboard visuel |
| `.devin/SKILLS-NETWORK.html` | Graphe interactif |
| `data/context-report.json` | Contexte detecte |
| `reports/validation-report.md` | Score et qualite |

## Commandes disponibles apres setup

```
/init-project-v2      — Meta-prompting V2 avec scoring
/brainstorm           — Atelier cahier des charges
/update-docs          — Synchronisation documentation
/validate-kit         — Scoring automatise 0-100
/wizard               — Mode interactif 8 etapes
/export-tools         — Export cross-platform
/analyze-context      — Detection automatique du contexte
/sync-docs            — Maintenance documentation
/generate-userguide   — Generation dashboards HTML
```

---

**Alias** : `/setup-windsurf` (raccourci)
