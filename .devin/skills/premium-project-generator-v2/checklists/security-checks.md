# Checklist Sécurité — PPG V2

## Scan automatisé (via `tools/scripts/security-scan.py`)

### Secrets et credentials
- [ ] Aucune clé AWS (AKIA*, ASIA*)
- [ ] Aucun token GitHub (ghp_*, gho_*, ghu_*)
- [ ] Aucun token Slack (xox*)
- [ ] Aucune clé API générique hardcodée
- [ ] Aucun Bearer token en clair
- [ ] Aucune clé privée (-----BEGIN PRIVATE KEY-----)
- [ ] Aucun mot de passe hardcodé
- [ ] Aucune URL de BDD avec credentials

### Fichiers sensibles
- [ ] Pas de fichiers .env (hors .env.example) dans le repo
- [ ] .gitignore inclut .env*
- [ ] Pas de fichiers de configuration avec secrets

### Configs MCP/RAG
- [ ] Tokens MCP via variables d'environnement
- [ ] Sources RAG sans credentials embarquées
- [ ] servers.json ne contient aucun token en clair

### Patterns d'injection
- [ ] Aucun eval() dans les scripts
- [ ] Aucun os.system()/subprocess avec interpolation non sécurisée
- [ ] Aucune concaténation SQL
- [ ] Aucune template injection

### Mode production
- [ ] Debug mode désactivé
- [ ] Pas de console.log/print de données sensibles
- [ ] Logs ne contiennent pas de PII

## Résultat

| Sévérité | Findings | Seuil |
|----------|----------|-------|
| HIGH | ___ | 0 (bloquant) |
| MEDIUM | ___ | ≤ 3 |
| LOW | ___ | informatif |
| **Score sécurité** | **___/10** | ≥ 7 pour premium |

## Commandes

```bash
# Scan complet
python3 tools/scripts/security-scan.py /path/to/kit

# Rapport JSON
python3 tools/scripts/security-scan.py /path/to/kit --json

# Auto-fix .gitignore
python3 tools/scripts/security-scan.py /path/to/kit --fix
```
