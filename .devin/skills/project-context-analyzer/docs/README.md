# Project Context Analyzer - Documentation

## Objectif

Ce skill est le **préambule** obligatoire de `premium-project-generator`. Il scanne
le workspace cible pour extraire automatiquement le contexte nécessaire à la
génération d'outils Windsurf.

## Workflow recommandé

```
Workspace cible
      │
      ▼
@project-context-analyzer
      │
      ├──► Scan filesystem (scan-workspace.js)
      ├──► Analyse textuelle (discovery-prompt.md + LLM)
      └──► Production du rapport (context-report.json)
      │
      ▼
Mise à jour mémoire du générateur
      │
      ▼
@premium-project-generator (lecture auto du contexte)
      │
      └──► Génération des outils adaptés
```

## Fichiers produits

| Fichier | Emplacement | Description |
|---------|-------------|-------------|
| Rapport brut | `.devin/skills/premium-project-generator/data/context-raw.json` | Données brutes du scan |
| Rapport analysé | `.devin/skills/premium-project-generator/data/context-report.json` | Rapport structuré prêt pour le générateur |
| Mémoire | `.devin/skills/premium-project-generator/memories/context.md` | Contexte mis à jour pour le générateur |

## Score de confiance

Le `confidence_score` indique la fiabilité des inférences :

- **90-100** : Manifeste + README clairs et complets. Peut lancer le générateur sans vérification.
- **70-89** : README présent mais manifeste absent (projet non-JS). Vérifier la stack.
- **50-69** : Aucun README, inférence par structure de dossiers. **Recommandé** : valider manuellement.
- **< 50** : Trop peu d'informations. Demander à l'utilisateur de compléter.

## Personnalisation

### Ajouter un nouveau framework
Modifier `data/stack-keywords.json` et ajouter les mots-clés dans la section
`frameworks` appropriée.

### Ajouter un domaine métier
Modifier `data/domain-keywords.json`. Les clés `primary` servent pour
l'analyse textuelle, `frameworks` pour la détection par dépendances.

## Dépannage

### Le script ne trouve pas git
Le script est tolerant : s'il n'y a pas de repo git, `git_contributors` sera
vide et la déduction `team_size` se fera sur la structure du projet.

### Projet sans manifeste (HTML/CSS pur)
Le skill se base sur les extensions de fichiers (`data/stack-keywords.json`
→ `runtimes`) et la structure des dossiers. Le `confidence_score` sera plus
bas mais l'analyse reste fonctionnelle.

### Mono-repo
Le script scanne la racine. Pour un mono-repo complexe, il peut être utile de
lancer le skill depuis un sous-package spécifique.

## Intégration avec premium-project-generator

Pour que le générateur lise automatiquement le rapport :

1. S'assurer que `data/context-report.json` existe à côté du générateur
2. Le générateur charge le JSON en Phase 0 (Discovery) pour pré-remplir les inputs
3. Si `confidence_score >= 80`, le générateur skip les questions de cadrage

## Maintenance

- Mettre à jour `data/stack-keywords.json` quand un nouveau framework devient populaire
- Mettre à jour `data/domain-keywords.json` quand un nouveau domaine métier émerge
- Vérifier que `data/context-output-schema.json` reste synchronisé avec le schéma d'input du générateur
