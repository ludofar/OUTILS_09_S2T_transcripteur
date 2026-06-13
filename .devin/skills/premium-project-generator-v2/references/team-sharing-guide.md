# Guide Partage Équipe — PPG V2

## Vue d'ensemble

Le Premium Project Generator V2 permet de partager automatiquement les outils
Windsurf générés avec toute l'équipe, via GitHub ou GitLab. L'objectif :
un collègue reçoit un one-liner et installe le kit en 30 secondes.

## Flux de partage

### 1. Détection de la plateforme Git

Le skill détecte automatiquement quelle plateforme utiliser :

```bash
# Vérifier GitHub CLI
gh auth status

# Vérifier GitLab CLI
glab auth status
```

**Logique de décision** :
- Si `gh` est disponible et authentifié → GitHub
- Si `glab` est disponible et authentifié → GitLab
- Si les deux sont disponibles → vérifier le remote `origin` du projet
  actuel pour inférer la plateforme de l'équipe
- Si aucun n'est disponible → instructions manuelles

### 2. Création du repo (automatique)

**GitHub** :
```bash
cd ./mon-kit-windsurf
git init
git add -A
git commit -m "feat: Kit Windsurf pour [project-name]"
gh repo create [project-name]-windsurf-tools --private --source=. --push
gh repo edit --add-topic windsurf-tools
```

**GitLab** :
```bash
cd ./mon-kit-windsurf
git init && git add -A && git commit -m "feat: Kit Windsurf pour [project-name]"
glab repo create [project-name]-windsurf-tools --private --defaultBranch main
git remote add origin <url>
git push -u origin main
glab repo edit --topic windsurf-tools
```

### 3. One-liner d'installation

Le skill génère un one-liner par plateforme cible :

```
Kit partagé ! Vos collègues peuvent l'installer avec :

  # Windsurf (projet)
  git clone <repo-url> .devin/tools/[project-name]-kit

  # Claude Code (global)
  git clone <repo-url> ~/.claude/skills/[project-name]-kit

  # Cursor (projet)
  git clone <repo-url> .cursor/rules/[project-name]-kit

  # Universal (Codex, Gemini, Kiro)
  git clone <repo-url> ~/.agents/skills/[project-name]-kit
```

### 4. Mise à jour

```bash
# Le collègue met à jour en un git pull
cd .devin/tools/[project-name]-kit && git pull
```

## Registre d'outils d'équipe

Pour les équipes avec 5+ outils partagés, le PPG V2 propose de créer
un **registre centralisé** — un repo Git qui catalogue tous les outils.

### Initialisation

```bash
python3 tools/scripts/team-registry.py init --name "Acme Corp Tools"
```

### Commandes du registre

```bash
# Publier un kit
python3 tools/scripts/team-registry.py publish ./mon-kit --tags frontend,nextjs

# Lister les outils disponibles
python3 tools/scripts/team-registry.py list

# Rechercher
python3 tools/scripts/team-registry.py search "frontend"

# Installer un outil
python3 tools/scripts/team-registry.py install kit-frontend

# Vérifier l'obsolescence
python3 tools/scripts/team-registry.py stale

# Détails d'un outil
python3 tools/scripts/team-registry.py info kit-frontend

# Supprimer
python3 tools/scripts/team-registry.py remove kit-frontend
```

### Guide d'onboarding équipe

Message type à partager sur Slack/Teams :

```
REGISTRE D'OUTILS WINDSURF — Quick Start

1. Cloner le registre (une seule fois) :
   git clone <registry-repo-url> ~/windsurf-tools-registry

2. Lister les outils disponibles :
   python3 team-registry.py list --registry ~/windsurf-tools-registry

3. Installer un outil :
   python3 team-registry.py install <nom> --registry ~/windsurf-tools-registry

4. Créer votre propre outil :
   @premium-project-generator-v2 avec vos variables projet

5. Publier au registre :
   python3 team-registry.py publish ./mon-kit --registry ~/windsurf-tools-registry --tags tag1,tag2
   cd ~/windsurf-tools-registry && git add -A && git commit -m "Add mon-kit" && git push
```

## Bonnes pratiques

1. **Repo privé par défaut** — Les outils contiennent des conventions internes
2. **Topic `windsurf-tools`** — Pour la découverte au sein de l'organisation
3. **Un repo par kit** — Plus simple à maintenir qu'un mono-repo
4. **Registre pour 5+ outils** — En dessous, le partage direct suffit
5. **Inclure install.sh** — Pour que les collègues n'aient rien à configurer
6. **Documenter** — README avec exemples d'invocation dans le kit partagé
