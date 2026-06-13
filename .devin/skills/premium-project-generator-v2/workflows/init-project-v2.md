---
description: Lance le meta-prompting V2 avec scoring 7 categories et generation complete des outils Windsurf
---

# Workflow : /init-project-v2

## Commande
```
/init-project-v2 [nom-projet] [stack-technique]
```

## Etapes

### 1. Contexte auto-detecte
- Verifier `data/context-report.json` (@project-context-analyzer)
- Si absent ou confidence < 80 : poser 3 questions maximum (nom, stack, domaine)

### 2. Execution du pipeline V2 (7 categories)

| Phase | Categorie | Outil | Sortie |
|-------|-----------|-------|--------|
| 1 | Securite | `tools/scripts/security-scan.py` | Rapport securite |
| 2 | Staleness | `tools/scripts/staleness-check.py` | Audit dependances/dates |
| 3 | Architecture | Meta-prompting niveau 2 | Blueprint complet |
| 4 | Generation | Meta-prompting niveau 3 | Fichiers generes |
| 5 | Validation | `tools/scripts/validate-kit.py` | Score 0-100 |
| 6 | Export | `tools/scripts/cross-platform-export.py` | Export 14 plateformes |
| 7 | Documentation | `@docs-auto-updater` | Sync documentation |

### 3. Scoring
- Afficher le score final par categorie
- Si score global < 70 : proposer corrections auto

### 4. Livrables
- `AGENTS.md` — Agents hierarchiques
- `.devin/rules/*.md` — 4+ rules adaptatives
- `.devin/skills/*/SKILL.md` — Skills metier + systeme
- `.devin/workflows/*.md` — Workflows manuels
- `.devin/rag/config.yaml` — Configuration RAG
- `.devin/integrations/mcp/servers.json` — Serveurs MCP

### 5. Finalisation
- `@docs-auto-updater` synchronise toute la documentation
- `@windsurf-userguide-generator` genere USERGUIDE.html + SKILLS-NETWORK.html
