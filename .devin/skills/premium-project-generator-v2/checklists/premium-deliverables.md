# Checklist Livrables Premium V2 (Valeur 2500€)

Ce checklist valide que le kit V2 justifie sa valeur premium augmentée.

## Livrables obligatoires (~500€ chacun)

### 1. AGENTS.md Hiérarchiques
- [ ] Racine avec guidelines générales
- [ ] Module principal avec conventions domaine
- [ ] Liens vers Rules et Skills
- [ ] **Métadonnées staleness** (V2)

### 2. Rules Adaptatives (4+ rules)
- [ ] coding-standards.md → glob
- [ ] domain-knowledge.md → model_decision
- [ ] review-checklist.md → manual
- [ ] security-guardrails.md → always_on
- [ ] Contextuelles au projet
- [ ] **Métadonnées staleness** (V2)

### 3. Skills Multi-étapes (3+ skills)
- [ ] Structure 14 dossiers où pertinent
- [ ] Frontmatter YAML complet
- [ ] Exemples input/output
- [ ] **Métadonnées staleness** (V2)

### 4. Workflows Manuels (3+ workflows)
- [ ] Invoquables via `/nom`
- [ ] Étapes claires
- [ ] **Métadonnées staleness** (V2)

## Livrables avancés V1 (+500€)

### 5. Configuration RAG
- [ ] config.yaml avec sources locales + distantes
- [ ] Requêtes prédéfinies métier

### 6. Configuration MCP
- [ ] servers.json valide
- [ ] Sécurité (tokens via env vars)

### 7. Documentation Auto-générée
- [ ] TOOLS_USERGUIDE.md générable
- [ ] Index par type d'outil

## Livrables V2 (+500€)

### 8. Security Scan (V2)
- [ ] Script security-scan.py fonctionnel
- [ ] Scan automatique de tous les livrables
- [ ] Rapport structuré (texte et JSON)
- [ ] Blocage sur findings HIGH

### 9. Staleness Check (V2)
- [ ] Script staleness-check.py fonctionnel
- [ ] Métadonnées injectées dans tous les fichiers
- [ ] Vérification review dates
- [ ] Support --check-deps et --check-drift

### 10. Cross-Platform Export (V2)
- [ ] Script cross-platform-export.py fonctionnel
- [ ] Export vers 14+ plateformes
- [ ] Conversion .mdc pour Cursor
- [ ] Conversion plain-md pour Cline/Roo/Trae
- [ ] INSTALL.md par plateforme

### 11. Partage Équipe (V2)
- [ ] Auto-détection GitHub/GitLab
- [ ] Création repo automatique
- [ ] One-liner d'installation
- [ ] Guide onboarding équipe

### 12. Scripts Validation Automatisée (V2)
- [ ] validate-kit.py remplace les checklists manuelles
- [ ] Score 0-100 calculé automatiquement
- [ ] Support --json pour CI/CD

### 13. Registre d'Outils (V2)
- [ ] team-registry.py fonctionnel
- [ ] init, publish, list, search, install, stale
- [ ] Catalogue partagé via Git

### 14. Mode Wizard (V2)
- [ ] Prompt wizard-interactive.md complet
- [ ] 8 étapes pas-à-pas
- [ ] Choix pré-définis avec défauts

### 15. install.sh Cross-Workspace (V2)
- [ ] Auto-détection 14 plateformes
- [ ] Options --global, --all, --dry-run, --uninstall
- [ ] Symlink ou copie selon OS

## Justification valeur V2

| Élément | Heures économisées | Valeur |
|---------|-------------------|--------|
| Setup AGENTS.md + Rules | 8h | 400€ |
| Création Skills + Workflows | 16h | 800€ |
| Config RAG + MCP | 8h | 400€ |
| Documentation + Guide | 4h | 200€ |
| **Security Scan (V2)** | **4h** | **200€** |
| **Staleness System (V2)** | **3h** | **150€** |
| **Cross-Platform Export (V2)** | **3h** | **150€** |
| **Team Sharing + Registry (V2)** | **2h** | **100€** |
| **Validation + Wizard (V2)** | **2h** | **100€** |
| **TOTAL** | **50h** | **2500€** |

## Validation finale

> Le kit V2 est "premium" uniquement si :
> - [ ] Tous les livrables obligatoires présents
> - [ ] Au moins 5 livrables V2 inclus
> - [ ] Score qualité ≥ 85/100
> - [ ] Security scan passé (0 HIGH)
> - [ ] Staleness metadata dans 100% des fichiers
> - [ ] L'utilisateur peut démarrer en < 30 min
