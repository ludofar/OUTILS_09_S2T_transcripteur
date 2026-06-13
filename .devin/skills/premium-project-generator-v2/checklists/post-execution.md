# Checklist Post-Exécution V2 — Premium Project Generator

## Validation des livrables générés

### AGENTS.md
- [ ] Fichier présent à la racine
- [ ] Structure hiérarchique
- [ ] Liens Rules/Skills corrects

### Rules (minimum 4)
- [ ] coding-standards.md — frontmatter + contenu
- [ ] domain-knowledge.md — frontmatter + contenu
- [ ] review-checklist.md — frontmatter + contenu
- [ ] security-guardrails.md — frontmatter + contenu
- [ ] Toutes ≤ 12k caractères
- [ ] Triggers valides
- [ ] **Métadonnées staleness présentes** (V2)

### Skills (minimum 3)
- [ ] Chemin `.devin/skills/<kebab-name>/SKILL.md` correct
- [ ] Frontmatter YAML complet et valide
- [ ] Progressive disclosure respectée
- [ ] **Métadonnées staleness présentes** (V2)

### Workflows (minimum 3)
- [ ] Invoquables via `/nom`
- [ ] Étapes numérotées claires
- [ ] **Métadonnées staleness présentes** (V2)

### RAG/MCP
- [ ] Configs générées si requises
- [ ] Pas de secrets en clair

## Validation V2

### Security Scan
- [ ] `python3 tools/scripts/security-scan.py` exécuté
- [ ] Score sécurité ≥ 7/10
- [ ] Aucun finding HIGH
- [ ] Rapport généré

### Staleness Check
- [ ] `python3 tools/scripts/staleness-check.py` exécuté
- [ ] Métadonnées présentes dans tous les fichiers
- [ ] Intervalles adaptés à la maturité
- [ ] Rapport généré

### Kit Validation
- [ ] `python3 tools/scripts/validate-kit.py` exécuté
- [ ] Score global ≥ 85/100
- [ ] Patches appliqués si nécessaire

### Cross-Platform Export (si demandé)
- [ ] `python3 tools/scripts/cross-platform-export.py` exécuté
- [ ] Fichiers convertis pour chaque plateforme cible
- [ ] INSTALL.md généré par plateforme
- [ ] install.sh inclus

### Team Sharing (si demandé)
- [ ] Repo créé (GitHub/GitLab)
- [ ] Code pushé
- [ ] Topic `windsurf-tools` ajouté
- [ ] One-liner d'installation communiqué

## Sauvegarde et documentation

- [ ] `memories/context.md` mis à jour
- [ ] `memories/preferences.md` sauvegardé
- [ ] `docs/README.md` documente le kit
- [ ] `docs/CHANGELOG.md` version initiale

## Métriques V2

| Métrique | Valeur |
|----------|--------|
| Rules générées | ___ |
| Skills générés | ___ |
| Workflows générés | ___ |
| Score validation | ___/100 |
| Score sécurité | ___/10 |
| Score staleness | ___/10 |
| Plateformes exportées | ___ |
| Temps de génération | ___ min |
