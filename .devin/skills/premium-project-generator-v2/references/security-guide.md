# Guide Sécurité — PPG V2

## Vue d'ensemble

Le Security Scan V2 analyse automatiquement tous les livrables générés
pour détecter les failles de sécurité courantes avant livraison.

## Catégories de détection

### 1. Secrets et credentials (HIGH)
- Clés API hardcodées (AWS, GitHub, Slack, etc.)
- Tokens Bearer en clair
- Clés privées embarquées
- URLs de base de données avec credentials
- Mots de passe en clair

### 2. Patterns d'injection (MEDIUM)
- Shell injection via interpolation de variables
- Usage de `eval()` ou `exec()`
- Concaténation SQL avec des inputs utilisateur
- Template injection

### 3. Configuration (MEDIUM/LOW)
- Tokens dans les configs MCP/RAG
- URLs avec credentials embarquées
- Mode debug activé en production
- Fichiers .env non gitignorés

## Utilisation

```bash
# Scan standard
python3 tools/scripts/security-scan.py /path/to/kit

# Rapport JSON (pour CI/CD)
python3 tools/scripts/security-scan.py /path/to/kit --json

# Auto-fix (.gitignore)
python3 tools/scripts/security-scan.py /path/to/kit --fix
```

## Niveaux de sévérité

| Sévérité | Impact | Action |
|----------|--------|--------|
| **HIGH** | Credential exposée | **Bloque la livraison** |
| **MEDIUM** | Pattern de risque | Avertissement, correction recommandée |
| **LOW** | Bonne pratique | Information, amélioration suggérée |

## Score de sécurité

- **100** : Aucun finding
- **85-99** : Uniquement LOW findings
- **50-84** : MEDIUM findings détectés
- **< 50** : HIGH findings — **livraison bloquée**

## Bonnes pratiques pour les livrables

1. **Variables d'environnement** — Toujours utiliser `${ENV_VAR}` pour les secrets
2. **MCP config** — Référencer les tokens via env vars dans `servers.json`
3. **RAG config** — Pas de credentials dans les sources d'indexation
4. **.gitignore** — Toujours inclure `.env*` (sauf `.env.example`)
5. **Documentation** — Mentionner les env vars requises dans le README
