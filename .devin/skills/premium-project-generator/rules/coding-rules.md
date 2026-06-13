---
name: "premium-coding-standards"
description: "Standards de codage pour les scripts et templates du générateur premium"
trigger: "glob: '**/*.{js,ts,json,yaml,yml}'"
priority: high
version: "1.0.0"
---

# Standards de Codage - Premium Project Generator

## JavaScript / Node.js

### Syntaxe
- Utiliser `const` par défaut, `let` si mutation nécessaire
- Jamais `var`
- Fonctions nommées pour la stack trace
- Arrow functions pour les callbacks courts

### Structure
```javascript
/**
 * Description de la fonction
 * @param {string} param1 - Description du paramètre
 * @returns {Object} Description du retour
 */
function validateSkill(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  // ...
  return { valid, errors };
}
```

### Modules
- Préférer ES modules (`import`/`export`)
- Sinon CommonJS (`require`/`module.exports`)
- Jamais mélanger les deux dans un même fichier

## JSON / YAML

### JSON
- 2 espaces d'indentation
- Clés triées alphabétiquement si pertinent
- Pas de trailing commas

### YAML
- 2 espaces d'indentation
- Pas de tabs
- Guillemets autour des chaînes avec caractères spéciaux
- Pipes `|` pour les descriptions multi-lignes

## Validation

### Schémas
- Tous les inputs doivent être validés avec JSON Schema
- Tous les outputs doivent être validés avec JSON Schema
- Les erreurs doivent être descriptives

### Tests
- Chaque script critique doit avoir un test minimal
- Les validators doivent tester les cas limites (edge cases)
