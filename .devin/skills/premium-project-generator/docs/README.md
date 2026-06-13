# Premium Project Generator

## Description

Skill **PREMIUM** pour générer automatiquement l'intégralité des outils Windsurf
(AGENTS.md, Rules, Skills, Workflows, RAG, MCP) pour tout nouveau projet.

**Valeur** : 2000€ | **Économie temps** : 40+ heures | **ROI** : 120-240%

## Structure du skill

```
premium-project-generator/
├── SKILL.md                          # Fichier principal
├── prompts/                          # Meta-prompting 4 niveaux
│   ├── level-1-analyzer.md
│   ├── level-2-architect.md
│   ├── level-3-generator.md
│   └── level-4-validator.md
├── tools/                            # Scripts, templates, generators
│   ├── scripts/
│   ├── templates/
│   ├── generators/
│   └── validators/
├── examples/                         # Cas d'usage
├── knowledge/                        # Guidelines et conventions
├── data/                             # Config, schemas, mappings
├── checklists/                       # Pre/post/quality/premium
├── memories/                         # Contexte et préférences
├── rules/                            # Coding et style rules
├── external/                         # Librairies externes
├── rag/                              # Sources RAG
├── integrations/                     # MCP et APIs
├── references/                       # Documentation et standards
├── workflows/                        # Sous-workflows internes
├── tests/                            # Cas de test et scénarios
└── docs/                             # Documentation
```

## Utilisation

### Invocation
```
@premium-project-generator
project_name: mon-projet
tech_stack: Next.js / TypeScript / Tailwind
business_domain: SaaS
team_size: small
maturity: MVP
```

### Phases d'exécution
1. **Discovery** → Cadrage et questions
2. **Analyse** (Niveau 1) → Diagnostic
3. **Architecture** (Niveau 2) → Blueprint
4. **Génération** (Niveau 3) → Fichiers
5. **Validation** (Niveau 4) → Quality gate
6. **Finalisation** → Documentation

## Livrables produits

- AGENTS.md hiérarchique
- 4+ Rules adaptatives
- 3+ Skills multi-étapes (structure 14 dossiers)
- 3+ Workflows manuels
- Config RAG (sources locales + distantes)
- Config MCP (serveurs pertinents)
- TOOLS_USERGUIDE.md auto-généré

## Dépendances

- Windsurf IDE avec Cascade
- Node.js 18+ (optionnel, pour les scripts)

## Licence

Produit premium - Usage commercial autorisé pour l'acheteur.
