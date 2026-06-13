# Guidelines V2 — Premium Project Generator

## Principes architecturaux

### 1. Meta-prompting hiérarchique
Le cœur du générateur est un système à 4 niveaux (Analyseur → Architecte → Générateur → Validateur). Chaque niveau produit un output structuré qui sert d'input au suivant. Ce chaînage garantit la cohérence et la qualité.

### 2. Clarity Principles (V2)
Les humains décrivent ce qu'ils *font*, pas ce qu'ils *ont besoin*. L'Analyseur V2 extrait les exigences implicites et surpasse la compréhension de l'utilisateur. La spécification produite contient des exigences que l'utilisateur ne pouvait pas articuler.

### 3. Progressive disclosure
Cascade ne charge que `name` et `description` par défaut. Le contenu complet n'est accessible qu'à l'invocation. Cette technique optimise le context window.

### 4. Context-driven generation
Chaque livrable est généré en fonction du contexte projet (stack, domaine, équipe, maturité). Un kit POC solo est très différent d'un kit production enterprise.

### 5. Security by default (V2)
Tous les livrables passent un scan de sécurité automatique. Aucun livrable avec un finding HIGH n'est livré. Les tokens et secrets sont systématiquement via variables d'environnement.

### 6. Staleness awareness (V2)
Chaque fichier généré embarque ses métadonnées d'obsolescence. Le système sait quand chaque outil doit être revu, et alerte proactivement.

### 7. Cross-platform portability (V2)
Un kit Windsurf n'est pas enfermé dans Windsurf. L'export automatique vers 14+ plateformes maximise la valeur des outils générés.

### 8. Standards enterprise-grade
Tous les livrables suivent les standards officiels Windsurf :
- Frontmatter YAML complet
- Kebab-case pour les identifiants
- Structure 14 dossiers lorsque pertinente
- Documentation en Français, code en Anglais

## Directrices de génération

### Priorisation MVP first
1. AGENTS.md et Rules fondamentales (bootstrap rapide)
2. Skills critiques (spécification, documentation)
3. Skills métier (contexte projet)
4. Workflows (orchestration manuelle)
5. RAG/MCP (enrichissement contextuel)
6. Documentation auto-générée (maintenance)
7. Export cross-platform (V2)
8. Partage équipe (V2)

### Sélection contextuelle des dossiers
L'Architecte (niveau 2) décide quels des 14 dossiers activer selon la complexité du skill, les besoins en connaissances, les intégrations, et la persistance requise.

### Qualité bloquante
Le Validateur V2 attribue un score global. Livraison bloquée si score < 85/100 OU si security scan a des findings HIGH.

## Anti-patterns

- ❌ Générer des fichiers génériques sans contexte projet
- ❌ Oublier la progressive disclosure (fichiers trop lourds)
- ❌ Commiter des tokens/secrets dans les configs MCP
- ❌ Créer des skills monolithiques (un skill = une responsabilité)
- ❌ Ignorer les checklists de validation
- ❌ Ne pas documenter les dépendances inter-skills
- ❌ **Omettre les métadonnées staleness** (V2)
- ❌ **Livrer sans security scan** (V2)
- ❌ **Ignorer les exigences implicites** (V2)
- ❌ **Limiter aux seuls utilisateurs Windsurf** sans export (V2)
