# Librairies Tierces et Vendored - Premium Project Generator

## Librairies vendored

Ce skill n'intègre pas de librairies vendored directement. Les dépendances
sont gérées via `external/packages/npm-references.json` et installées
optionnellement par l'utilisateur.

## Librairies externes recommandées

### Validation YAML
- **Lib** : js-yaml / yaml (npm)
- **Usage** : Parsing des frontmatter des skills, rules et workflows
- **Alternative** : PyYAML (si scripts Python)

### Validation JSON Schema
- **Lib** : ajv (npm) / jsonschema (Python)
- **Usage** : Validation des inputs/outputs du générateur
- **Note** : Les schémas dans `tools/validators/` utilisent Draft-07

### Template Engine
- **Lib** : Handlebars (npm) / Jinja2 (Python)
- **Usage** : Génération des fichiers à partir des templates dans `tools/templates/`
- **Alternative** : String replacement simple si pas de librairie

### Filesystem
- **Lib** : fs-extra (npm) / shutil (Python)
- **Usage** : Scaffolding, copie de templates, création d'arborescence

## Gestion des dépendances

### Option 1 : Package.json dédié
Créer un `package.json` dans le dossier du skill :
```json
{
  "name": "premium-project-generator-deps",
  "dependencies": {
    "yaml": "^2.3.0",
    "ajv": "^8.12.0"
  }
}
```

### Option 2 : Global install
Installer les packages globalement sur la machine.

### Option 3 : Mode dégradé
Le skill fonctionne sans dépendances externes en utilisant :
- `JSON.parse` pour le JSON
- Regex basiques pour le YAML simple
- `fs` natif pour le filesystem

## Recommandation

Pour une utilisation premium (valeur 2000€), il est recommandé
d'installer au minimum `yaml` et `ajv` pour garantir la fiabilité
des validations.
