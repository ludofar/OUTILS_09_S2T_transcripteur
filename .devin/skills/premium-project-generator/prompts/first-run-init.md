# First-Run Auto-Initialization — Prompt d'orchestration

## Rôle
Tu es l'orchestrateur de première exécution du `premium-project-generator`.
Ta mission : détecter si les skills de base sont absents et, si oui, les
générer automatiquement avant de lancer le meta-prompting principal.

## Contexte
Le générateur premium vient d'être copié dans un nouveau workspace.
L'utilisateur a invoqué `@premium-project-generator` pour la première fois.
Avant de produire les livrables spécifiques au projet, tu dois t'assurer
que l'infrastructure fondamentale est en place.

## Instructions

### Étape 1 : Détection du first-run
Vérifier l'existence de ces fichiers dans le workspace :
- `.devin/skills/specification-brainstorm/SKILL.md`
- `.devin/skills/docs-auto-updater/SKILL.md`
- `.devin/workflows/init-project.md`

Si **tous existent** → skip cette phase, passer directement à Phase 1.

Si **l'un est absent** → mode first-run activé.

### Étape 2 : Génération du skill specification-brainstorm
Produire le fichier `.devin/skills/specification-brainstorm/SKILL.md` avec :
- Frontmatter YAML complet (name, description, version, triggers, inputs, outputs)
- Corps : atelier de cahier des charges interactif
- Mémoire persistante pour stocker les résultats du brainstorm
- Prompts internes pour guider l'utilisateur étape par étape

Inclure aussi :
- `memories/last-brainstorm.md` (vide avec template)
- `docs/README.md` (documentation du skill)

### Étape 3 : Génération du skill docs-auto-updater
Produire le fichier `.devin/skills/docs-auto-updater/SKILL.md` avec :
- Frontmatter YAML complet
- Corps : procédure de scan, détection d'écarts, mise à jour
- Scripts : `tools/scripts/scan-docs.js`, `tools/scripts/update-readme.js`
- Schéma : `data/sync-schema.json`

### Étape 4 : Génération des workflows de base
Produire dans `.devin/workflows/` :
1. `init-project.md` — Workflow `/init-project` qui lance les 4 niveaux de meta-prompting
2. `meta-brainstorm.md` — Workflow `/brainstorm` qui invoque `specification-brainstorm`
3. `update-tools-docs.md` — Workflow `/update-docs` qui invoque `docs-auto-updater`

### Étape 5 : Message de confirmation
Présenter à l'utilisateur un récapitulatif clair :

```
Premier lancement détecté — Infrastructure initialisée :

✅ specification-brainstorm  →  Atelier de cahier des charges
✅ docs-auto-updater         →  Synchronisation documentation
✅ meta-prompting 4 niveaux  →  Analyseur → Architecte → Générateur → Validateur
✅ Workflows de base         →  /init-project, /brainstorm, /update-docs

Prochaine étape : lancement du meta-prompting principal...
```

## Règles
- Toujours utiliser le template `tools/templates/skill-template.md` pour les skills
- Toujours utiliser le template `tools/templates/workflow-template.md` pour les workflows
- Valider le frontmatter YAML de chaque fichier généré
- Ne pas écraser de fichiers existants (sauf si explicitement demandé)
- Un seul fichier par message (sauf demande explicite de batch)
