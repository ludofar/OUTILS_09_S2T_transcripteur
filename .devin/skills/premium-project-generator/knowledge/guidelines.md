# Guidelines - Premium Project Generator

## Principes architecturaux

### 1. Meta-prompting hiérarchique
Le cœur du générateur est un système à 4 niveaux (Analyseur → Architecte → Générateur → Validateur). Chaque niveau produit un output structuré qui sert d'input au suivant. Ce chaînage garantit la cohérence et la qualité.

### 2. Progressive disclosure
Cascade ne charge que `name` et `description` par défaut. Le contenu complet n'est accessible qu'à l'invocation. Cette technique optimise le context window et permet d'avoir de nombreux skills sans surcharge.

### 3. Context-driven generation
Chaque livrable est généré en fonction du contexte projet (stack, domaine, équipe, maturité). Un kit pour un POC solo en React sera très différent d'un kit production pour une équipe de 15 en microservices.

### 4. Standards enterprise-grade
Tous les livrables suivent les standards officiels Windsurf :
- Frontmatter YAML complet
- Kebab-case pour les identifiants
- Structure 14 dossiers lorsque pertinente
- Documentation en Français, code en Anglais

### 5. Valeur justifiée
Le tarif de 2000€ est justifié par :
- 40+ heures d'ingénierie manuelle économisées
- Qualité enterprise-grade des livrables
- Maintenance auto-documentée
- Évolutivité du kit généré

## Directrices de génération

### Priorisation MVP first
1. AGENTS.md et Rules fondamentales (bootsrap rapide)
2. Skills critiques (spécification, documentation)
3. Skills métier (contexte projet)
4. Workflows (orchestration manuelle)
5. RAG/MCP (enrichissement contextuel)
6. Documentation auto-générée (maintenance)

### Sélection contextuelle des dossiers
Pas tous les 14 dossiers sont nécessaires pour chaque skill. L'Architecte (niveau 2) décide quels dossiers activer selon :
- Complexité du skill
- Besoins en connaissances
- Intégrations externes nécessaires
- Persistance de contexte requise

### Qualité bloquante
Le Validateur (niveau 4) attribue un score global. Livraison bloquée si score < 85/100. Les patches doivent être appliqués avant finalisation.

## Anti-patterns

- ❌ Générer des fichiers génériques sans contexte projet
- ❌ Oublier la progressive disclosure (fichiers trop lourds)
- ❌ Commiter des tokens/secrets dans les configs MCP
- ❌ Créer des skills monolithiques (un skill = une responsabilité)
- ❌ Ignorer les checklists de validation
- ❌ Ne pas documenter les dépendances inter-skills
