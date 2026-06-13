---
description: Mode wizard interactif 8 etapes pour configurer un projet Windsurf de A a Z
---

# Workflow : /wizard

## Commande
```
/wizard
```

## Etapes interactives

### Etape 1 — Nom et identite
- Nom du projet (kebab-case)
- Description en une phrase
- Domaine metier (e-commerce, SaaS, EdTech...)

### Etape 2 — Stack technique
- Framework frontend (Next.js, Astro, SvelteKit...)
- Backend (Node, Python, Go...)
- Base de donnees (PostgreSQL, Mongo, Supabase...)
- Hote (Vercel, Netlify, AWS...)

### Etape 3 — Equipe et maturite
- Taille de l'equipe (solo, petite, moyenne, grande)
- Niveau de maturite (prototype, MVP, production)
- Langues supportees

### Etape 4 — Outils Windsurf souhaites
- [ ] AGENTS.md hierarchiques
- [ ] Rules adaptatives
- [ ] Skills metier personnalises
- [ ] Workflows operations
- [ ] RAG interne
- [ ] MCP servers

### Etape 5 — Qualite et securite
- [ ] Activer Security Scan
- [ ] Activer Staleness Check
- [ ] Activer le scoring automatise

### Etape 6 — Export et partage
- [ ] Exporter vers Cursor (.mdc)
- [ ] Exporter vers Claude Code
- [ ] Exporter vers GitHub Copilot
- [ ] Publier sur le registre equipe

### Etape 7 — Generation
Lancer `@premium-project-generator-v2` avec tous les parametres collectes.

### Etape 8 — Validation
Afficher le score et proposer corrections si besoin.

---

Le wizard lit `prompts/wizard-interactive.md` pour les questions et la logique de navigation.
