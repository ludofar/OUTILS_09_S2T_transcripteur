# Matrice de Compatibilité Stacks

## Web / Fullstack

| Stack | Rules suggérées | Skills suggérés | MCP | RAG |
|-------|----------------|-----------------|-----|-----|
| Next.js / TypeScript | `coding-standards-ts.md`, `nextjs-conventions.md` | `project-scaffold`, `debug-analyzer`, `component-generator` | filesystem, github, postgres | docs Next.js, shadcn/ui |
| Astro / MDX | `coding-standards-ts.md`, `astro-conventions.md` | `project-scaffold`, `content-manager` | filesystem | docs Astro, MDX spec |
| React / Vite | `coding-standards-js.md`, `react-patterns.md` | `project-scaffold`, `component-generator` | filesystem, github | docs React |
| Vue / Nuxt | `coding-standards-js.md`, `vue-conventions.md` | `project-scaffold`, `component-generator` | filesystem | docs Vue |
| Svelte / SvelteKit | `coding-standards-js.md`, `svelte-conventions.md` | `project-scaffold` | filesystem | docs Svelte |

## Backend / API

| Stack | Rules suggérées | Skills suggérés | MCP | RAG |
|-------|----------------|-----------------|-----|-----|
| Python / FastAPI | `coding-standards-py.md`, `fastapi-patterns.md` | `project-scaffold`, `api-generator` | filesystem, postgres | docs FastAPI, Pydantic |
| Python / Django | `coding-standards-py.md`, `django-conventions.md` | `project-scaffold`, `api-generator` | filesystem, postgres | docs Django |
| Node.js / Express | `coding-standards-js.md`, `express-patterns.md` | `project-scaffold`, `api-generator` | filesystem, postgres | docs Express |
| Go / Gin | `coding-standards-go.md`, `go-conventions.md` | `project-scaffold`, `api-generator` | filesystem, postgres | docs Go |
| Rust / Actix | `coding-standards-rs.md`, `rust-patterns.md` | `project-scaffold` | filesystem | docs Rust |

## Mobile

| Stack | Rules suggérées | Skills suggérés | MCP | RAG |
|-------|----------------|-----------------|-----|-----|
| Flutter / Dart | `coding-standards-dart.md` | `project-scaffold` | filesystem | docs Flutter |
| React Native | `coding-standards-ts.md` | `project-scaffold`, `component-generator` | filesystem | docs React Native |
| SwiftUI | `coding-standards-swift.md` | `project-scaffold` | filesystem | docs Apple |
| Kotlin / Compose | `coding-standards-kt.md` | `project-scaffold` | filesystem | docs Android |

## Data / ML

| Stack | Rules suggérées | Skills suggérés | MCP | RAG |
|-------|----------------|-----------------|-----|-----|
| Python / Pandas | `coding-standards-py.md`, `data-pipeline.md` | `project-scaffold`, `data-validator` | filesystem, postgres | docs Pandas |
| Python / PyTorch | `coding-standards-py.md`, `ml-patterns.md` | `project-scaffold`, `model-trainer` | filesystem, postgres | docs PyTorch |
| Rust / Polars | `coding-standards-rs.md`, `data-pipeline.md` | `project-scaffold` | filesystem | docs Polars |

## DevOps / Infrastructure

| Stack | Rules suggérées | Skills suggérés | MCP | RAG |
|-------|----------------|-----------------|-----|-----|
| Terraform | `coding-standards-hcl.md`, `iac-patterns.md` | `project-scaffold`, `infra-deployer` | filesystem, github | docs Terraform |
| Docker / K8s | `docker-patterns.md`, `k8s-conventions.md` | `project-scaffold`, `deploy-pipeline` | filesystem, github | docs Kubernetes |
| GitHub Actions | `ci-patterns.md`, `gha-conventions.md` | `project-scaffold` | filesystem, github | docs GitHub Actions |

## Notes

- **MCP filesystem** : Presque toujours pertinent (accès fichiers)
- **MCP github** : Utile pour référencer des repos et templates
- **MCP postgres** : Pertinent si base de données dans le stack
- **RAG docs** : Toujours indexer la documentation officielle du framework principal
