---
description: "Initialiser un nouveau projet avec le kit d'outils Windsurf complet"
---

# /init-project

## Objectif
Générer l'intégralité des outils Windsurf pour un nouveau projet en
utilisant le Premium Project Generator.

## Prérequis
- Variables projet définies (name, stack, domaine) ou rapport `context-report.json`
- Windsurf IDE ouvert
- Skill `premium-project-generator` disponible
- Skills de base initialisés (auto-en first-run)

## Étapes

### 1. Lancer le générateur

**Commande** : `@premium-project-generator`

En first-run, le générateur auto-initialise les skills de base.
Ensuite, il charge automatiquement le contexte depuis `data/context-report.json`
s'il est disponible.

**Input** (optionnel si context-report présent) :
```
project_name: mon-projet
tech_stack: Next.js / TypeScript
business_domain: SaaS
team_size: small
maturity: MVP
```

### 2. Phase Discovery + First-Run Init

- **First-Run** (si détecté) : Génération auto de `specification-brainstorm`, `docs-auto-updater`, workflows `/brainstorm` et `/update-docs`
- **Discovery** : Chargement du rapport contexte ou questions de clarification (max 3)

### 3. Phase Analyse (auto)

- Attendre le rapport `analysis_report.json`
- Vérifier que le stack est correctement identifié

### 4. Phase Architecture (auto)

- Réviser le blueprint proposé
- Confirmer les dossiers activer (14 types)
- Confirmer MCP et RAG recommandés

### 5. Phase Génération (auto)

- Suivre la génération fichier par fichier
- Valider chaque livrable avant passage au suivant

### 6. Phase Validation (auto)

- Vérifier le score global (minimum 85/100)
- Appliquer les patches si nécessaire

### 7. Finalisation + Sync Documentation

- Générer `TOOLS_USERGUIDE.md`
- **Invoquer** `@docs-auto-updater` pour synchroniser la documentation
- Mettre à jour les mémoires
- Archiver le contexte

## Checklist de sortie

- [ ] AGENTS.md présent à la racine
- [ ] 4+ Rules dans `.devin/rules/`
- [ ] 3+ Skills dans `.devin/skills/`
- [ ] 3+ Workflows dans `.devin/workflows/`
- [ ] Config RAG dans `.devin/rag/`
- [ ] Config MCP dans `.devin/integrations/mcp/`
- [ ] Score de validation ≥ 85/100

## Liens

- Skill principal : `@premium-project-generator`
- Documentation : `docs/README.md`
