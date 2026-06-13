---
description: Exporte le kit Windsurf genere vers 14+ plateformes (Cursor, Claude Code, Copilot, Codex, Gemini...)
---

# Workflow : /export-tools

## Commande
```
/export-tools [format] [chemin-destination]
```

## Formats supportes

| Plateforme | Extension | Commande |
|------------|-----------|----------|
| Cursor | `.mdc` | `/export-tools cursor` |
| Claude Code | `.md` | `/export-tools claude` |
| GitHub Copilot | `.prompt` | `/export-tools copilot` |
| Codex CLI | `.yaml` | `/export-tools codex` |
| Gemini CLI | `.json` | `/export-tools gemini` |
| VS Code Snippets | `.code-snippets` | `/export-tools vscode` |
| All | mixed | `/export-tools all` |

## Etapes

### 1. Validation pre-export
- Verifier que `validate-kit.py` score >= 60
- Si < 60 : bloquer l'export, proposer corrections

### 2. Conversion
Executer `tools/scripts/cross-platform-export.py` avec les bons arguments.

### 3. Verification post-export
- Lister les fichiers generes
- Verifier la taille et l'integrite

### 4. Livraison
- Afficher les chemins des fichiers exportes
- Proposer un commit git avec message standardise
