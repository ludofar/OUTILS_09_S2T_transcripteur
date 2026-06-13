# Guide Détection Obsolescence — PPG V2

## Vue d'ensemble

Les outils Windsurf deviennent obsolètes. Les APIs changent, les conventions
évoluent, les règles réglementaires se mettent à jour. Le Staleness Check V2
détecte ces dérives avant qu'elles n'impactent les utilisateurs.

## Trois couches de détection

### 1. Review tracking (dates de révision)
Chaque fichier généré inclut des métadonnées de staleness :

```yaml
metadata:
  created: 2026-05-22
  last_reviewed: 2026-05-22
  review_interval_days: 90
```

Le checker compare `last_reviewed + review_interval_days` à la date actuelle.

**Statuts** :
| Statut | Jours depuis review | Action |
|--------|-------------------|--------|
| FRESH | 0-60 | Aucune |
| AGING | 61-90 | Planifier une review |
| STALE | 91-180 | Review urgente |
| CRITICAL | 180+ | Rework obligatoire |

### 2. Dependency health (santé des dépendances)
Les fichiers peuvent déclarer des dépendances externes :

```yaml
dependencies:
  - url: https://api.example.com/v1
    name: Example API
    type: api
  - url: https://docs.nextjs.org
    name: Next.js docs
    type: documentation
```

Le flag `--check-deps` vérifie que chaque URL est accessible (HTTP 2xx/3xx).

### 3. Schema drift (dérive de schéma)
Pour les APIs, on peut déclarer les clés attendues :

```yaml
schema_expectations:
  - url: https://api.example.com/v1/data
    method: GET
    expected_keys:
      - id
      - name
      - value
```

Le flag `--check-drift` compare les clés réelles aux clés attendues.

## Utilisation

```bash
# Vérification des dates de review
python3 tools/scripts/staleness-check.py /path/to/project

# + Santé des dépendances
python3 tools/scripts/staleness-check.py /path/to/project --check-deps

# + Dérive de schéma
python3 tools/scripts/staleness-check.py /path/to/project --check-drift

# Rapport JSON
python3 tools/scripts/staleness-check.py /path/to/project --json
```

## Intervalles recommandés par maturité

| Maturité | Intervalle | Raison |
|----------|-----------|--------|
| POC | 30 jours | Change constamment |
| MVP | 60 jours | Stabilisation en cours |
| Production | 90 jours | Stable, revue trimestrielle |
| Legacy migration | 45 jours | Transition active |

## Intégration avec le registre d'équipe

```bash
# Vérifier l'obsolescence de tous les outils du registre
python3 tools/scripts/team-registry.py stale
```

## Bonnes pratiques

1. **Toujours injecter** `metadata.created` et `metadata.last_reviewed`
2. **Mettre à jour** `last_reviewed` après chaque review manuelle
3. **Déclarer** les dépendances externes pour le health check
4. **Adapter** l'intervalle selon la maturité du projet
5. **Automatiser** le check dans CI/CD pour les équipes
