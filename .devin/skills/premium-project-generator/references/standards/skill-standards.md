# Standards et Spécifications Applicables

## Standards Windsurf Skills

### Format SKILL.md
- **Source** : https://agentskills.io/home
- **Version** : Current
- **Requis** :
  - Frontmatter YAML avec `name` et `description`
  - Corps en Markdown
  - Référence aux fichiers support via chemins relatifs

### Nommage
- **Convention** : kebab-case (minuscules, chiffres, tirets)
- **Exemples valides** : `premium-project-generator`, `debug-analyzer`
- **Exemples invalides** : `PremiumProject`, `debug_analyzer`

### Scopes
- **Workspace** : `.devin/skills/` (commité, projet spécifique)
- **Global** : `~/.codeium/windsurf/skills/` (machine, non commité)
- **System** : `C:\ProgramData\Windsurf\skills\` (IT, read-only)

## Standards de Code

### JavaScript/Node.js
- **ESLint** : Config `eslint:recommended`
- **Prettier** : 2 espaces, 100 car, trailing commas
- **Tests** : Vitest ou Jest, couverture > 80%

### Shell Scripts
- **Shellcheck** : Validation statique bash/sh
- **set -euo pipefail** : Fail fast strict mode
- **Logging** : Couleurs et niveaux (INFO/WARN/ERROR)

## Standards de Documentation

### Markdown
- **Frontmatter** : YAML pour métadonnées
- **Titres** : H2 pour sections, H3 pour sous-sections
- **Listes** : Préférer les listes à puces aux paragraphes denses
- **Code** : Fenced blocks avec langage

### JSON/YAML
- **JSON** : Formattez avec 2 espaces
- **YAML** : Pas de tabs, indentation cohérente
- **Schémas** : Référencer `$schema` quand applicable

## Standards de Sécurité

### Secrets
- **Interdit** : Aucun secret dans les fichiers du skill
- **Variables d'environnement** : Utiliser `${ENV_VAR}`
- **Fichiers sensibles** : Ajouter à `.gitignore`

### Validation
- **Inputs** : Toujours valider avec JSON Schema
- **Scripts** : Pas d'exécution de code arbitraire
- **Templates** : Échapper les variables utilisateur

## Standards de Performance

### Taille du skill
- **SKILL.md** : < 500 lignes idéalement
- **Ressources** : Charger à la demande (lazy loading)
- **Mémoire** : Ne pas stocker de gros blobs dans `memories/`

### Context Window
- **Progressive disclosure** : Réduire le contenu initial
- **Références** : Pointer vers des fichiers plutôt qu'inliner
- **Checklists** : Courtes et actionnables

## Standards Premium (Spécifiques 2000€)

### Justification valeur
- Documenter le temps économisé (40+ heures)
- Calculer le ROI (120-240%)
- Démontrer la qualité enterprise-grade

### Qualité bloquante
- Score minimum : 85/100
- Checklists pré/post exécution
- Validation automatique des frontmatter
- Patches et correctifs intégrés

### Livrables complets
- AGENTS.md hiérarchique
- 4+ Rules adaptatives
- 3+ Skills multi-étapes (14 dossiers)
- 3+ Workflows manuels
- Config RAG + MCP
- Documentation auto-générée

---

**Compliance** : Ce skill suit tous ces standards
**Vérification** : `checklists/quality-checks.md`
