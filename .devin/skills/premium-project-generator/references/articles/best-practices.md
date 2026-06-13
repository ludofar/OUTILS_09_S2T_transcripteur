# Best Practices - Premium Project Generator

## Architecture de Skills Premium

### "How to Create Effective AI Skills"
**Source** : Windsurf Docs + pratique
**Résumé** :
- Progressive disclosure : name + description visibles, contenu chargé à l'invocation
- Un skill = une responsabilité principale
- Documenter les dépendances inter-skills
- Versionner avec semver

### "Meta-Prompting for Code Generation"
**Source** : Internal knowledge
**Résumé** :
- 4 niveaux de raisonnement : analyse → architecture → génération → validation
- Chaînage JSON structuré entre niveaux
- Qualité bloquante (score minimum)
- Feedback loop entre niveaux

## Patterns et Anti-patterns

### ✅ Patterns recommandés
1. **Skill composition** : Un skill peut invoquer d'autres skills via @mention
2. **Template inheritance** : Templates de base + overrides spécifiques
3. **Schema-driven** : Valider tout input/output avec JSON Schema
4. **Memory-augmented** : Persister le contexte entre sessions
5. **Checklist-guarded** : Checklists pré/post pour qualité
6. **Context-driven** : Adapter les livrables au stack/domaine/équipe
7. **Value-justified** : Documenter la valeur économique du kit

### ❌ Anti-patterns à éviter
1. **Skill monolithique** : Un skill qui fait trop de choses
2. **Prompt stuffing** : Trop de contexte dans le prompt initial
3. **Hard-coded paths** : Chemins absolus dans les scripts
4. **Silent failures** : Pas de validation des sorties
5. **No documentation** : Skill sans README ni exemples
6. **Generic output** : Livrables non adaptés au contexte projet
7. **Secret leakage** : Tokens/secrets commités dans les configs

## Intégrations avancées

### MCP + Skills
- MCP étend les capacités du skill avec des outils externes
- Exemple : Serveur filesystem pour validation, GitHub pour templates
- Configurer dans `integrations/mcp/servers.json`

### Knowledge Base + RAG
- Windsurf Knowledge Base (Beta) permet l'indexation
- Le skill peut définir ses propres sources dans `rag/config.yaml`
- Requêtes prédéfinies pour les cas d'usage fréquents

## Métriques et amélioration

### Comment mesurer un skill premium
1. **Score de validation** : ≥ 85/100
2. **Temps de génération** : < 1h pour un kit complet
3. **Économie temps** : 40+ heures économisées
4. **ROI** : > 120% pour un MVP, > 200% pour production

### Itération
- Capturer les échecs dans `memories/history.md`
- Ajuster les prompts basé sur les erreurs
- Enrichir les exemples avec les cas réels

---

**Dernière mise à jour** : 2026-05-19
**Prochaine revue** : 2026-06-19
