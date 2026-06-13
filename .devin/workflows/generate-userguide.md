---
description: Genere ou met a jour le USERGUIDE.html et le SKILLS-NETWORK.html du dossier .devin/
---

# Workflow : Generate UserGuide

## Commande
```
/generate-userguide [chemin-optionnel]
```

## Étapes

### 1. Discovery — Scanner le dossier .devin/

Scanner le contenu du dossier `.devin/` (ou celui spécifié en argument).

Extraire pour chaque catégorie :

**Skills (`skills/*/SKILL.md`) :**
- Nom du skill (dossier)
- Titre (frontmatter `title` ou `# Titre`)
- Description (frontmatter `description` ou premier paragraphe)
- Workflows embarqués (`skills/*/workflows/*.md`)
- Chemin relatif

**Workflows (`workflows/*.md`) :**
- Nom du fichier (sans .md)
- Titre (frontmatter ou `# Titre`)
- Description
- Skill lié (si mentionné dans le contenu)
- Catégorie implicite (déduite du nom : blog, seo, ui, traduction, etc.)

**Rules (`rules/*.md`) :**
- Nom du fichier
- Titre
- Description courte
- État (ok/warn) — déduit du contenu (ex: "interdiction" → warn, "checklist" → ok)
- Progression estimée (%) — basée sur la maturité du contenu

**Agents (`agents.md` ou `agents/*.md`) :**
- Nom de l'agent
- Rôle
- Description
- Skills liés
- Workflows liés
- Famille (design, seo, content, i18n, etc.)

**Guides (`guides/*.md` ou `guide-*.md`) :**
- Nom du fichier
- Titre
- Description
- Nombre de pages estimé (basé sur la taille du contenu)
- Catégorie

**Config (`config.*`, `prompts/`) :**
- Nom du fichier
- Description

### 2. Structuration — Organiser les donnees

Compter les elements par categorie pour les stats du hero.

Organiser les workflows par categorie (Content, Traduction, SEO, UI/UX, Lexique, Orchestration).

Organiser les agents par famille (Design & UI, Content & SEO, Traduction & i18n, etc.).

Construire le **graphe de relations skills** pour SKILLS-NETWORK.html :
- Extraire les relations entre skills depuis les SKILL.md
- Assigner un type de lien a chaque connexion : ORCHESTRATE, FLOWS_TO, ALIMENTE, VALIDE, DEPEND, MARKETING
- Assigner une categorie a chaque skill
- Generer les noeuds (position initiale par categorie) et les liens (source, cible, type)

### 3. Génération HTML — Creer les deux fichiers

**USERGUIDE.html** — Dashboard principal :

Générer un fichier HTML unique et autonome avec la structure complète :

**Template HTML à générer :**

```html
<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UserGuide — [Nom du Projet]</title>
  <style>
    /* CSS complet avec : */
    /* - Variables CSS dark/light */
    /* - Reset et base */
    /* - Layout (container, sections) */
    /* - Hero (titre, recherche, stats, compteurs animés) */
    /* - Navigation sticky avec underline animé */
    /* - Cards premium (badge, hover glow, favoris) */
    /* - Flow cards (Relations) */
    /* - Kanban (Workflows) */
    /* - Checklist (Rules) avec barres de progression */
    /* - Org chart (Agents) avec familles collapsibles */
    /* - Library (Guides) avec cartes livre */
    /* - View toggle (compact / détaillé) */
    /* - Detail popup */
    /* - Dark/Light mode toggle */
    /* - Animations (fadeInUp, morphing) */
    /* - Responsive */
  </style>
</head>
<body>
  <button class="theme-toggle" id="theme-toggle">🌙</button>

  <header class="hero">
    <h1>[Nom du Projet]</h1>
    <p>[Description extraite du README]</p>
    <div class="search-bar">
      <svg>...</svg>
      <input type="text" id="global-search" placeholder="Rechercher...">
    </div>
    <div class="stats">
      <div class="stat"><div class="num">[N]</div><div class="lbl">Skills</div></div>
      <!-- ... -->
    </div>
  </header>

  <div class="sticky-nav">
    <!-- 7 tabs : Relations, Overview, Skills, Workflows, Rules, Agents, Guides -->
  </div>

  <main class="container">
    <!-- RELATIONS -->
    <section id="relations" class="section active">
      <!-- Flow cards détaillées -->
    </section>

    <!-- SKILLS -->
    <section id="skills" class="section">
      <!-- Cards -->
    </section>

    <!-- WORKFLOWS -->
    <section id="workflows" class="section">
      <div class="section-header">
        <!-- Toggle : Kanban / Cards -->
      </div>
      <div class="view-content active" data-view="compact">
        <!-- Kanban -->
      </div>
      <div class="view-content" data-view="detailed">
        <!-- Cards détaillées -->
      </div>
    </section>

    <!-- RULES -->
    <section id="rules" class="section">
      <div class="section-header">
        <!-- Toggle : Checklist / Cards -->
      </div>
      <div class="view-content active" data-view="compact">
        <!-- Checklist -->
      </div>
      <div class="view-content" data-view="detailed">
        <!-- Cards détaillées -->
      </div>
    </section>

    <!-- AGENTS -->
    <section id="agents" class="section">
      <div class="section-header">
        <!-- Toggle : Organigramme / Cards -->
      </div>
      <div class="view-content active" data-view="compact">
        <!-- Org chart -->
      </div>
      <div class="view-content" data-view="detailed">
        <!-- Cards détaillées -->
      </div>
    </section>

    <!-- GUIDES -->
    <section id="guides" class="section">
      <div class="section-header">
        <!-- Toggle : Bibliothèque / Cards -->
      </div>
      <div class="view-content active" data-view="compact">
        <!-- Library -->
      </div>
      <div class="view-content" data-view="detailed">
        <!-- Cards détaillées -->
      </div>
    </section>
  </main>

  <script>
    // JavaScript complet avec :
    // - Tab navigation avec morphing
    // - Dark/Light mode (localStorage)
    // - Recherche globale
    // - Favoris (localStorage)
    // - View toggles
    // - Detail popups
    // - Animated counters
  </script>
</body>
</html>
```

### 3b. SKILLS-NETWORK.html — Graphe relationnel interactif

- SVG avec physique de forces (repulsion, attraction, damping)
- Noeuds draggables avec `pinned` pendant le drag
- Mode Focus : clic sur un skill pour l'isoler et voir ses connexions
- Panel lateral affichant les flux entrants et sortants
- Liens colores par type avec styles pleins/pointilles
- Tooltip au survol, double-clic pour reset, touche Escape
- Aucune dependance externe

### 4. Sauvegarde

Écrire les deux fichiers a :
```
[chemin]/.devin/USERGUIDE.html
[chemin]/.devin/SKILLS-NETWORK.html
```

### 5. Confirmation

Indiquer à l'utilisateur :
- Le chemin du fichier généré
- Le nombre d'éléments détectés par catégorie
- Un résumé des vues disponibles

## Règles de génération

1. **HTML autonome** : Aucune ressource externe (CDN, images, fonts). Tout est inline.
2. **Dark mode par défaut** : `data-theme="dark"` sur `<html>`
3. **Données dynamiques** : Toutes les données sont injectées directement dans le HTML au moment de la génération
4. **Fichier unique** : Le résultat est un seul fichier `.html`
5. **Pas de build requis** : Ouvrir le fichier dans un navigateur suffit

## Exemple de sortie

```
✅ USERGUIDE.html genere
✅ SKILLS-NETWORK.html genere
📍 .devin/USERGUIDE.html
📍 .devin/SKILLS-NETWORK.html
📊 Contenu detecte :
   • 23 Skills
   • 43 Workflows
   • 19 Rules
   • 18 Agents
   • 9 Guides
🎨 Vues disponibles (USERGUIDE.html) :
   • Relations (flow cards)
   • Skills (cards)
   • Workflows (Kanban ↔ Cards)
   • Rules (Checklist ↔ Cards)
   • Agents (Org Chart ↔ Cards)
   • Guides (Bibliotheque ↔ Cards)
🕸️  Graphe interactif (SKILLS-NETWORK.html) :
   • Noeuds draggables, physique de forces
   • Mode Focus + panel lateral
   • Liens colores par type
⚙️ Fonctionnalités :
   • Recherche globale, Favoris, Dark/Light mode, Popups détails
```

## Mise à jour

Pour mettre à jour après des changements dans `.devin/` :
```
/generate-userguide
```

Le fichier existant est écrasé avec les données à jour.
