# Exemple d'usage basique - Premium Project Generator

## Scénario : Nouveau projet Next.js

### Contexte
- **Nom** : `ma-super-app`
- **Stack** : Next.js 14 / TypeScript / Tailwind
- **Domaine** : SaaS B2B
- **Équipe** : small (3 développeurs)
- **Maturité** : MVP
- **Contraintes** : RGPD, i18n (fr, en), accessibilité

### Invocation

```
@premium-project-generator
project_name: ma-super-app
tech_stack: Next.js 14 / TypeScript / Tailwind
business_domain: SaaS B2B
team_size: small
maturity: MVP
constraints: [RGPD, i18n, accessibilité]
languages: [fr, en]
```

### Phase 1 : Discovery
Cascade pose 3 questions :
1. Quel framework CSS ? → Tailwind confirmé
2. Besoin de SSR/SSG ? → SSR avec SSG pour landing
3. Base de données ? → PostgreSQL via Prisma

### Phase 2 : Analyse (Niveau 1)
Output : `analysis_report.json`
- Type : web fullstack
- Langages : TypeScript
- Frameworks : Next.js, React, Tailwind, Prisma
- Risques : RGPD → besoin de rule spécifique

### Phase 3 : Architecture (Niveau 2)
Output : `architecture_blueprint.json`
- 4 Rules : coding-standards-ts, saas-knowledge, review-checklist, rgpd-guardrails
- 4 Skills : specification-brainstorm, tools-documentation, component-generator, api-routes
- 5 Workflows : /init-project, /meta-brainstorm, /update-tools-docs, /create-component, /api-review
- MCP : filesystem, github, postgres
- RAG : docs Next.js, docs Prisma, docs Tailwind

### Phase 4 : Génération (Niveau 3)
Génération fichier par fichier :
1. `AGENTS.md` → Racine + src/
2. `.devin/rules/coding-standards-ts.md`
3. `.devin/rules/saas-knowledge.md`
4. `.devin/rules/review-checklist.md`
5. `.devin/rules/rgpd-guardrails.md`
6. `.devin/skills/specification-brainstorm/SKILL.md` (structure 14 dossiers)
7. ... [etc]

### Phase 5 : Validation (Niveau 4)
Score : 92/100
- ✅ Frontmatter YAML complets
- ✅ Progressive disclosure respectée
- ✅ Intégrations MCP/RAG documentées
- ⚠️ Skill `component-generator` pourrait avoir plus d'exemples

### Phase 6 : Finalisation
- `TOOLS_USERGUIDE.md` généré
- `memories/context.md` mis à jour
- Checklist post-exécution validée

## Résultat final

Le projet `ma-super-app` dispose maintenant de :
- 1 AGENTS.md hiérarchique
- 4 Rules adaptatives
- 4 Skills multi-étapes
- 5 Workflows manuels
- Config RAG avec sources locales et distantes
- Config MCP avec filesystem, github, postgres
- Documentation auto-générée

**Temps total** : ~45 minutes
**Économie estimée** : 40+ heures de travail manuel
