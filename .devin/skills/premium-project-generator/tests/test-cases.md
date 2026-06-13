# Cas de Test - Premium Project Generator

## Test 1 : Bootstrap projet web

### Input
```json
{
  "project_name": "test-web-app",
  "tech_stack": "Next.js / TypeScript / Tailwind",
  "business_domain": "saas",
  "team_size": "small",
  "maturity": "MVP"
}
```

### Steps attendues
1. Phase Discovery : 3 questions max
2. Phase Analyse : Stack identifié comme "web fullstack"
3. Phase Architecture : 4 Rules, 4 Skills, 5 Workflows
4. Phase Génération : Tous les fichiers créés
5. Phase Validation : Score ≥ 85/100

### Critères de succès
- [ ] AGENTS.md présent
- [ ] 4 Rules avec frontmatter valide
- [ ] 4 Skills avec structure 14 dossiers
- [ ] 5 Workflows invoquables via `/`
- [ ] Config RAG et MCP générées
- [ ] Score ≥ 85

---

## Test 2 : Projet backend API

### Input
```json
{
  "project_name": "test-api",
  "tech_stack": "Python / FastAPI / PostgreSQL",
  "business_domain": "fintech",
  "team_size": "medium",
  "maturity": "production",
  "constraints": ["RGPD", "PCI-DSS"]
}
```

### Critères de succès
- [ ] Rules supplémentaires RGPD et PCI-DSS
- [ ] Skills avec validation renforcée
- [ ] MCP postgres activé
- [ ] RAG sources docs FastAPI + PostgreSQL

---

## Test 3 : Legacy migration

### Input
```json
{
  "project_name": "legacy-modernize",
  "tech_stack": "React / Vite / TypeScript",
  "business_domain": "ecommerce",
  "team_size": "large",
  "maturity": "legacy-migration"
}
```

### Critères de succès
- [ ] Analyse legacy incluse
- [ ] Plan de migration documenté
- [ ] Rules adaptées à la transition
- [ ] Skills de migration créés

---

## Test 4 : Validation frontmatter

### Script
```bash
node tools/scripts/validate-frontmatter.js .devin/rules/coding-standards.md
```

### Critères de succès
- [ ] YAML valide
- [ ] Champs obligatoires présents
- [ ] Trigger valide
- [ ] Taille ≤ 12k

---

## Test 5 : Progressive disclosure

### Vérification
1. Lire le prompt système de Cascade
2. Confirmer que seuls `name` et `description` sont visibles
3. Vérifier que le contenu complet n'est chargé qu'à l'invocation

### Critères de succès
- [ ] Description visible sans invocation
- [ ] SKILL.md complet chargé après @mention
