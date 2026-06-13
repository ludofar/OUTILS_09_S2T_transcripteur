---
name: windsurf-userguide-generator
version: 1.1.0
description: Genere un USERGUIDE.html premium et un SKILLS-NETWORK.html interactif a partir du dossier .devin/ d'un projet
author: Yin Shi
---

# Windsurf UserGuide Generator

## Vue d'ensemble

Ce skill scanne le dossier `.devin/` d'un projet et génère un fichier `USERGUIDE.html` complet, premium et interactif — un dashboard visuel de l'architecture Windsurf du projet.

**Ce qui est scanné :**
- `agents.md` et `agents/` — Définition des agents
- `skills/` — Skills avec leur SKILL.md et workflows embarqués
- `workflows/` — Workflows racine (.md)
- `rules/` — Rules opérationnelles (.md)
- `guides/` — Guides thématiques (.md)
- Configs : `config.*`, `prompts/`, etc.

**Ce qui est généré :**
Deux fichiers HTML autonomes (zéro dépendance externe) :

1. **`USERGUIDE.html`** — Dashboard principal avec :
- Recherche globale en temps réel
- Vue Relations avec flow cards détaillées
- Vue Skills en cards premium
- Vue Workflows en Kanban + toggle Cards détaillées
- Vue Rules en checklist + toggle Cards détaillées
- Vue Agents en organigramme + toggle Cards détaillées
- Vue Guides en bibliothèque + toggle Cards détaillées
- Dark/Light mode avec persistance localStorage
- Favoris ⭐ avec persistance localStorage
- Popups de détails sur chaque élément
- Animations et micro-interactions

2. **`SKILLS-NETWORK.html`** — Diagramme relationnel interactif des skills avec :
- **Nœuds draggables** avec physique de forces (attraction/répulsion)
- **Mode Focus** : clic sur un skill pour l'isoler et voir ses connexions
- **Panel latéral** affichant les flux entrants et sortants du skill sélectionné
- **Liens colorés par type** : ORCHESTRE (or plein), ALIMENTE (bleu pointillé), VALIDE (vert plein), DEPEND (gris pointillé), MARKETING (rose plein)
- **Tooltip au survol** avec description du skill
- **Double-clic** n'importe où pour revenir à la vue globale
- **Touche Escape** pour fermer le mode Focus
- Skills regroupés visuellement par catégorie (Experts, Validation, Pedagogie, Gestion, etc.)

## Utilisation

### Commande
```
/generate-userguide [chemin-optionnel]
```

- Sans argument : scanne `.devin/` du workspace courant
- Avec argument : scanne le dossier `.devin/` spécifié

### Output
```
.devin/USERGUIDE.html
.devin/SKILLS-NETWORK.html
```

## Architecture du générateur

### Phase 1 : Discovery
1. Lister le contenu de `.devin/`
2. Parser les frontmatter des fichiers `.md`
3. Extraire les métadonnées (titres, descriptions, badges, relations)
4. Compter les éléments par catégorie

### Phase 2 : Structuration
Organiser les données en 7 sections :
1. **Relations** — Flux de données entre agents, skills et workflows
2. **Skills** — Capacités avec workflows liés
3. **Workflows** — Procédures opérationnelles par catégorie
4. **Rules** — Règles avec état de conformité
5. **Agents** — Agents par famille
6. **Guides** — Documentation thématique
7. **Config** — Fichiers de configuration

### Phase 2b : Graphe de relations Skills
Construire le graphe relationnel pour `SKILLS-NETWORK.html` :
- Extraire les relations entre skills depuis les SKILL.md (`RELATES_TO`, `DEPENDS_ON`, `VALIDATES`, `CALLS`, `OUTPUTS_TO`)
- Ou inférer les liens depuis les descriptions et les workflows embarques
- Assigner un type de lien a chaque connexion : `ORCHESTRATE`, `FLOWS_TO`, `ALIMENTE`, `VALIDE`, `DEPEND`, `MARKETING`
- Assigner une categorie a chaque skill : `orchestration`, `pedagogie`, `experts`, `validation`, `base`, `gestion`, `marketing`, `technique`
- Generer les nœuds (position initiale par categorie) et les liens (source, cible, type)

### Phase 3 : Rendu HTML
Generer **deux** fichiers HTML autonomes :

**USERGUIDE.html** :
- CSS inlined (dark/light mode, animations, grid layouts)
- JavaScript inlined (recherche, favoris, toggles, popups, dark mode)
- Aucune dépendance externe

**SKILLS-NETWORK.html** :
- SVG avec physique de forces (repulsion, attraction, damping)
- Nœuds draggables avec `pinned` pendant le drag
- Mode Focus : clic → isolation + panel lateral avec flux entrants/sortants
- Liens colorés par type avec styles pleins/pointilles
- Tooltip au survol, double-clic pour reset, touche Escape
- Aucune dépendance externe

## Spécifications du SKILLS-NETWORK.html généré

### Architecture du graphe
- **Nœuds** : un par skill, positionnes par categorie (gauche/droite/haut/bas)
- **Liens** : extraits des relations declarees dans les SKILL.md ou inferes
- **Physique** : repulsion entre nœuds, attraction par les liens, gravity vers position initiale, damping 0.88
- **Pinning** : un nœud drague est fige (`pinned = true`) jusqu'au relachement

### Interactions
| Action | Comportement |
|--------|-------------|
| **Clic** sur un nœud | Mode Focus : nœud pulse, liens actives colores, autres grises, panel lateral s'ouvre avec flux entrants/sortants |
| **Clic** sur une relation dans le panel | Navigation vers le skill lie (focus change) |
| **Glisser** un nœud | Repositionnement libre, physique suspendue pour ce nœud |
| **Double-clic** n'importe où | Reset complet, panel ferme, vue globale |
| **Escape** | Reset |
| **Survol** d'un nœud (sans focus) | Tooltip description + highlight subtil des voisins |

### Types de liens
| Type | Couleur | Style | Signification |
|------|---------|-------|---------------|
| `ORCHESTRATE` | `#D4AF37` | Plein | Orchestrateur vers agent executeur |
| `FLOWS_TO` | `#8b5cf6` | Plein | Flux de travail sequentiel |
| `ALIMENTE` | `#4A90E2` | Pointille | Base de connaissances vers expert |
| `VALIDE` | `#2D9D6F` | Plein | Skill vers validateur |
| `DEPEND` | `#64748b` | Pointille fin | Dependance fonctionnelle |
| `MARKETING` | `#f43f5e` | Plein | Promotion ou export |

### Panel lateral (320px)
- Titre du skill + badge categorie colore
- Description complete
- Section **Flux sortants** : liste des skills cibles avec type de lien
- Section **Flux entrants** : liste des skills sources avec type de lien
- Clic sur un skill de la liste = navigation

## Spécifications du USERGUIDE.html généré

### Navigation
- Barre sticky avec 7 onglets + indicateur animé
- Morphing fade+translateY entre les sections

### Command Center (Hero)
- Titre du projet extrait du README ou du dossier
- Barre de recherche globale filtrant tout le contenu
- Compteurs animés (skills, workflows, rules, agents, guides)

### Vue Relations
- 3 flow cards détaillées avec :
  - Déclencheur (`/commande`)
  - Chaîne d'agents (→ séparés)
  - Workflows liés (badges)
  - Rules appliquées
  - Output final

### Vue Skills
- Cards avec badge, titre, chemin, description, relations workflows

### Vue Workflows
- **Toggle** : Kanban (compact) / Cards (détaillé)
- Kanban : 6 colonnes par catégorie
- Cards : description complète, badge, chemin

### Vue Rules
- **Toggle** : Checklist (compact) / Cards (détaillé)
- Checklist : indicateur ✅/⚠️, barre de progression
- Cards : description complète, badge, chemin

### Vue Agents
- **Toggle** : Organigramme (compact) / Cards (détaillé)
- Organigramme : familles collapsibles
- Cards : description, skills liés, workflows

### Vue Guides
- **Toggle** : Bibliothèque (compact) / Cards (détaillé)
- Bibliothèque : cartes livre avec couverture emoji
- Cards : description complète, badge

### Interactions
- **Dark/Light mode** : toggle ☀️/🌙, persistance localStorage
- **Favoris** : ⭐ sur chaque card, persistance localStorage
- **Recherche** : filtre tout le contenu en temps réel
- **Popups** : clic sur n'importe quel élément → modal avec détails
- **Animations** : hover scale/glow, compteurs animés, morphing de section

## Dépendances

Aucune. Les deux fichiers HTML sont 100 % autonomes (CSS et JS inlined).

## Fichiers produits

| Fichier | Description |
|---------|-------------|
| `USERGUIDE.html` | Dashboard HTML autonome, premium, interactif |
| `SKILLS-NETWORK.html` | Diagramme relationnel interactif des skills (graphe physique, mode focus, panel lateral)

## Maintenance

Pour mettre à jour le guide après des changements dans `.devin/` :
```
/generate-userguide
```

Les fichiers `USERGUIDE.html` et `SKILLS-NETWORK.html` sont ecrases avec les donnees fraiches.
