---
description: Analyse le workspace pour extraire le contexte projet (stack, domaine, equipe, maturite) et produire un rapport structure
---

# Workflow : /analyze-context

## Commande
```
/analyze-context [chemin-optionnel]
```

## Etapes

### 1. Scan du workspace
- Lister les fichiers a la racine
- Detecter package.json, requirements.txt, Cargo.toml...
- Identifier le framework et le langage

### 2. Detection automatique
- `tools/scripts/scan-workspace.js` analyse la structure
- `data/stack-keywords.json` et `data/domain-keywords.json` fournissent les mappings

### 3. Rapport
Produire `data/context-report.json` avec :
- `project_name`, `tech_stack`, `business_domain`
- `team_size`, `maturity`, `constraints`, `languages`
- `confidence_score` (0-100)

### 4. Utilisation
Ce rapport est consomme par `@premium-project-generator` et `@premium-project-generator-v2`
pour pre-remplir les inputs Phase 0.

---

**Dependance** : `@project-context-analyzer`
