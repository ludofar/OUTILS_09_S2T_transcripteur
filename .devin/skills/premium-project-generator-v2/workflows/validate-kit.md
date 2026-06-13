---
description: Valide le kit Windsurf genere avec scoring automatise 0-100 sur 7 categories
---

# Workflow : /validate-kit

## Commande
```
/validate-kit [chemin-projet]
```

## Etapes

### 1. Execution du script
```bash
python tools/scripts/validate-kit.py --path . --report
```

### 2. Analyse des resultats
Le script evalue 7 categories (total 100 points) :

| Categorie | Poids | Criteres |
|-----------|-------|----------|
| Structure | 25% | Fichiers obligatoires, arborescence correcte |
| Securite | 15% | Pas de cles hardcodees, pas d'injection |
| Qualite | 15% | Frontmatter valide, progressive disclosure |
| Completeness | 15% | Skills, rules, workflows, agents presents |
| Documentation | 10% | README, guides, TROUBLESHOOTING |
| Portabilite | 10% | Export cross-platform fonctionnel |
| Maintenance | 10% | Dates de review, freshness |

### 3. Rapport actionnable
- Afficher le score par categorie avec barres de progression
- Lister les echecs avec chemin du fichier et correction suggeree
- Si score >= 80 : kit valide pour production
- Si score 60-79 : corrections recommandees
- Si score < 60 : refaire la generation

### 4. Export du rapport
- `reports/validation-report.json` — Donnees brutes
- `reports/validation-report.md` — Rapport lisible
