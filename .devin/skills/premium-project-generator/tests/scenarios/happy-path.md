# Scénario Happy Path - Premium Project Generator

## Contexte
Utilisateur expérimenté avec Windsurf, variables bien définies.

## Déroulement

### Étape 1 : Invocation
```
@premium-project-generator
project_name: saas-dashboard
tech_stack: Next.js 14 / TypeScript / Prisma / PostgreSQL
business_domain: SaaS B2B
team_size: small
maturity: MVP
constraints: [RGPD, i18n]
languages: [fr, en]
```

### Étape 2 : Discovery (30s)
Cascade pose 2 questions :
1. "Framework CSS ?" → Tailwind
2. "ORM ?" → Prisma confirmé

### Étape 3 : Analyse (1min)
Rapport généré automatiquement :
- Stack : web fullstack
- Langages : TypeScript
- Risques : RGPD → rule spécifique requise

### Étape 4 : Architecture (2min)
Blueprint proposé :
- 5 Rules : coding-standards-ts, saas-knowledge, review-checklist, rgpd-guardrails, i18n-rules
- 5 Skills : specification-brainstorm, tools-documentation, component-generator, api-routes, auth-module
- 6 Workflows : /init-project, /meta-brainstorm, /update-tools-docs, /create-component, /api-review, /auth-setup
- MCP : filesystem, github, postgres
- RAG : docs Next.js, docs Prisma, docs PostgreSQL

### Étape 5 : Génération (20min)
Génération fichier par fichier, validation entre chaque.

### Étape 6 : Validation (3min)
Score : 91/100
- ✅ Frontmatter complets
- ✅ Progressive disclosure
- ✅ Intégrations documentées
- ⚠️ Skill auth-module : ajouter exemple OAuth

### Étape 7 : Finalisation (2min)
- TOOLS_USERGUIDE.md généré
- Memories mises à jour
- Checklist post-exécution validée

## Résultat
Kit complet généré en ~30 minutes.
Économie estimée : 45 heures de travail manuel.

## Critères de succès
- [ ] Temps total < 45 min
- [ ] Score ≥ 85/100
- [ ] Tous les livrables présents
- [ ] Utilisateur satisfait
