---
description: "Activer l'orchestrateur meta-prompting pour exploration complexe"
---

# /meta-brainstorm

## Objectif
Utiliser le système de meta-prompting à 4 niveaux pour explorer une
problématique complexe (architecture, refactoring, feature design).

## Prérequis
- Contexte suffisamment défini
- Skill `specification-brainstorm` initialisé (auto-en first-run)

## Étapes

### 1. Définir l'objectif

Formuler clairement ce que l'on cherche à explorer :
- Architecture d'une nouvelle feature
- Refactoring d'un module existant
- Choix technologiques
- Cahier des charges d'un nouveau module

### 2. Activer le skill de brainstorming

**Commande** : `@specification-brainstorm`

**Input** (exemple) :
```
objective: "Explorer l'architecture d'un système de notifications temps réel"
context: "Projet Next.js avec PostgreSQL et Redis"
constraints: ["scalabilité", "fiabilité", "coût"]
```

### 3. Suivre l'atelier interactif

- Le skill pose des questions ciblées (max 3 par tour)
- Il structure les réponses en sections : besoin, contraintes, solution, plan
- La mémoire `memories/last-brainstorm.md` conserve les décisions

### 4. Appliquer les résultats

- Documenter les décisions dans `AGENTS.md`
- Créer les rules et skills nécessaires via `@premium-project-generator`
- Mettre à jour les mémoires

## Checklist de sortie

- [ ] Rapport d'analyse complet
- [ ] Blueprint architectural validé
- [ ] Spécifications générées
- [ ] Score de validation ≥ 85/100

## Liens

- Skill : `@premium-project-generator`
- Prompts : `prompts/level-*`
