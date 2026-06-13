# Checklist Livrables Premium (Valeur 2000€)

Ce checklist valide que le kit généré justifie sa valeur premium.

## Livrables obligatoires ( valeur ~500€ chacun )

### 1. AGENTS.md Hiérarchiques
- [ ] Racine avec guidelines générales
- [ ] Module principal (src/) avec conventions domaine
- [ ] Sous-modules si architecture complexe
- [ ] Liens explicites vers Rules et Skills
- [ ] Instructions sur les mémoires à créer

### 2. Rules Adaptatives (4+ rules)
- [ ] `coding-standards.md` → glob sur extensions stack
- [ ] `domain-knowledge.md` → model_decision
- [ ] `review-checklist.md` → manual
- [ ] `security-guardrails.md` → always_on
- [ ] Chaque rule est contextuelle au projet (pas générique)
- [ ] Taille ≤ 12k caractères

### 3. Skills Multi-étapes (3+ skills)
- [ ] Structure 14 dossiers où pertinent
- [ ] Meta-prompting interne si complexe
- [ ] Frontmatter YAML complet
- [ ] Templates et generators
- [ ] Exemples input/output
- [ ] Intégrations RAG et MCP documentées

### 4. Workflows Manuels (3+ workflows)
- [ ] Invoquables via `/nom`
- [ ] Frontmatter YAML avec description
- [ ] Étapes claires et actionnables
- [ ] Référence aux skills et rules
- [ ] Checklist de sortie

## Livrables avancés (+500€ de valeur)

### 5. Configuration RAG
- [ ] `rag/config.yaml` avec sources locales + distantes
- [ ] Requêtes prédéfinies métier
- [ ] Boosting des fichiers pertinents
- [ ] Intégration Windsurf Knowledge Base

### 6. Configuration MCP
- [ ] `integrations/mcp/servers.json` valide
- [ ] Serveurs pertinents pour le stack
- [ ] Sécurité (pas de tokens en clair)
- [ ] Points d'intégration documentés

### 7. Librairies Externes
- [ ] `external/repositories/github-sources.md`
- [ ] `external/packages/npm-references.json`
- [ ] Justification de chaque référence

### 8. Documentation Auto-générée
- [ ] `TOOLS_USERGUIDE.md` générable
- [ ] Index par tags et type d'outil
- [ ] Fiche par outil (activation, objectif, exemple)

## Justification valeur

| Élément | Heures économisées | Valeur estimée |
|---------|-------------------|----------------|
| Setup manuel AGENTS.md + Rules | 8h | 400€ |
| Création Skills + Workflows | 16h | 800€ |
| Config RAG + MCP | 8h | 400€ |
| Documentation + Guide | 8h | 400€ |
| **TOTAL** | **40h** | **2000€** |

## Validation finale

> Le kit est considéré "premium" uniquement si :
> - [ ] Tous les livrables obligatoires sont présents
> - [ ] Au moins 3 livrables avancés sont inclus
> - [ ] Score de qualité ≥ 85/100
> - [ ] L'utilisateur peut démarrer le projet en < 30 min
