# Template AGENTS.md V2

## Usage
Copier ce template à la racine du projet et personnaliser selon le contexte.

## Structure

```markdown
# {{PROJECT_NAME}} - AGENTS.md

## Rôle & Mission

Tu es l'agent principal du projet **{{PROJECT_NAME}}**.
Domaine : {{BUSINESS_DOMAIN}}
Stack : {{TECH_STACK}}

## Contexte d'activation

Cet agent est actif pour :
- Tout fichier du projet (always-on)
- Décisions architecturales (model_decision)
- Revues de code (manual trigger via @review-checklist)

## Règles associées

- `coding-standards.md` → Glob sur `**/*.{extensions}`
- `domain-knowledge.md` → Model decision
- `review-checklist.md` → Manual
- `security-guardrails.md` → Always on

## Skills disponibles

- `@specification-brainstorm` → Atelier cahier des charges
- `@tools-documentation` → Génération guide utilisateur
- `@[skill-metier]` → [Description skill métier]

## Mémoires à créer

Utiliser `create_memory` pour persister :
- [ ] Architecture décisionnelle validée
- [ ] Conventions de nommage du projet
- [ ] Points de friction identifiés
- [ ] Préférences utilisateur (style doc, langue)

## Conventions spécifiques

{{CONVENTIONS_SPECIFIQUES}}

## Exemples

### Exemple 1 : [Cas d'usage]
```
[Input] → [Output attendu]
```

---

**Version** : {{VERSION}}
**Dernière mise à jour** : {{DATE}}
**Metadata staleness** :
  created: {{DATE}}
  last_reviewed: {{DATE}}
  review_interval_days: {{INTERVAL}}
  generator: premium-project-generator-v2
```

## Variables à remplacer
- `{{PROJECT_NAME}}` : Nom du projet
- `{{BUSINESS_DOMAIN}}` : Domaine métier
- `{{TECH_STACK}}` : Stack technique
- `{{CONVENTIONS_SPECIFIQUES}}` : Conventions propres au projet
- `{{VERSION}}` : Version du AGENTS.md
- `{{DATE}}` : Date de dernière mise à jour
- `{{INTERVAL}}` : Intervalle de review en jours (30/60/90/45 selon maturité)
