# Troubleshooting - Premium Project Generator

## Problèmes courants

### "Skill non détecté par Cascade"

**Cause** : Chemin incorrect ou frontmatter invalide

**Solution** :
1. Vérifier le chemin : `.devin/skills/premium-project-generator/SKILL.md`
2. Valider le YAML du frontmatter
3. Vérifier que `name` et `description` sont bien définis
4. Redémarrer Windsurf

### "Score de validation < 85"

**Cause** : Livrables incomplets ou frontmatter manquants

**Solution** :
1. Lire le rapport `data/validation-report.json`
2. Appliquer les patches proposés
3. Vérifier les checklists `checklists/quality-checks.md`
4. Relancer la phase de génération

### "Templates non trouvés"

**Cause** : Chemin relatif incorrect depuis le skill

**Solution** :
1. Vérifier que `tools/templates/` existe
2. Utiliser des chemins relatifs au dossier du skill
3. Exemple : `tools/templates/skill-template.md`

### "RAG sources indisponibles"

**Cause** : URLs distantes inaccessibles

**Solution** :
1. Vérifier la connexion internet
2. Consulter `rag/sources/index.md` pour les URLs
3. Passer en mode dégradé (sources locales uniquement)
4. Mettre à jour `rag/config.yaml` si URL changée

### "MCP serveurs non connectés"

**Cause** : Configuration incorrecte ou serveur non démarré

**Solution** :
1. Vérifier `integrations/mcp/servers.json`
2. S'assurer que les variables d'environnement sont définies
3. Ne jamais commiter de tokens/secrets
4. Tester la connexion manuellement

### "Variables projet ambiguës"

**Cause** : Inputs insuffisants pour l'analyse

**Solution** :
1. Répondre aux 3 questions de Discovery
2. Utiliser les valeurs par défaut si acceptable
3. Consulter `data/stack-mappings.json` pour les stacks connus

### "Conflit de noms de skills"

**Cause** : Deux skills avec le même nom dans différents scopes

**Solution** :
1. Utiliser le scope workspace pour le projet
2. Renommer le skill (kebab-case différent)
3. Vérifier `~/.codeium/windsurf/skills/` pour les conflits globaux

## Erreurs spécifiques

### "YAML parse error in frontmatter"

**Diagnostic** :
```bash
node tools/scripts/validate-frontmatter.js [fichier]
```

**Correction** :
- Vérifier l'indentation (2 espaces, pas de tabs)
- Échapper les caractères spéciaux
- Utiliser des guillemets pour les chaînes complexes

### "Schema validation failed"

**Diagnostic** :
Comparer le fichier contre `tools/validators/skill-schema.json`

**Correction** :
- Ajouter les champs manquants
- Vérifier les types des valeurs
- Respecter les enums (scope, trigger modes)

## Support

Pour des problèmes non listés ici :
1. Consulter `references/documentation/windsurf-docs.md`
2. Vérifier `knowledge/guidelines.md`
3. Lire les exemples dans `examples/`
4. Examiner les logs de validation
