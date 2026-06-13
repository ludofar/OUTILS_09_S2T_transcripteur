# Scénarios Edge Cases - Premium Project Generator

## Cas 1 : Variables incomplètes

### Contexte
Utilisateur fournit seulement `project_name` et `tech_stack`.

### Comportement attendu
1. Phase Discovery : poser les questions manquantes
2. Si ambiguïté persiste : utiliser valeurs par défaut
   - `team_size` → "small"
   - `maturity` → "MVP"
   - `constraints` → []
3. Génération continue sans blocage

### Validation
- [ ] Questions posées ≤ 3
- [ ] Valeurs par défaut documentées
- [ ] Kit généré malgré inputs partiels

---

## Cas 2 : Stack inconnu / exotique

### Contexte
`tech_stack` = "Elm / Haskell / Nix"

### Comportement attendu
1. Phase Analyse : stack non reconnu dans `data/stack-mappings.json`
2. Fallback sur règles génériques
3. Avertissement utilisateur : "Stack peu commun, livrables génériques proposés"
4. Proposer d'enrichir `data/stack-mappings.json`

### Validation
- [ ] Aucune erreur bloquante
- [ ] Livrables génériques générés
- [ ] Message d'avertissement clair

---

## Cas 3 : Conflit de noms

### Contexte
Projet avec nom identique à un skill existant.

### Comportement attendu
1. Détection du conflit
2. Suggestion de renommage
3. Ou utilisation de scope différent (workspace vs global)

### Validation
- [ ] Conflit détecté
- [ ] Solution proposée
- [ ] Pas d'écrasement non voulu

---

## Cas 4 : Frontmatter invalide

### Contexte
Génération produit un SKILL.md avec YAML syntaxiquement invalide.

### Comportement attendu
1. Validateur (niveau 4) détecte l'erreur
2. Score impacté (< 85)
3. Patch proposé avec correction YAML
4. Génération ne peut pas être validée sans correction

### Validation
- [ ] Erreur détectée
- [ ] Score reflète la qualité
- [ ] Patch applicable

---

## Cas 5 : RAG sources indisponibles

### Contexte
Sources RAG distantes (URLs) indisponibles (404, timeout).

### Comportement attendu
1. Détection de l'indisponibilité
2. Fallback sur sources locales uniquement
3. Avertissement utilisateur
4. Génération continue avec RAG dégradé

### Validation
- [ ] Pas de blocage
- [ ] Fallback actif
- [ ] Message utilisateur
