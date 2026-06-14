# Contexte Persistant - Premium Project Generator

## Dernier projet généré

- **Nom** : transcripteur
- **Stack** : Python 3.11, Poetry, Typer, Rich, faster-whisper, onnxruntime, torchaudio, ffmpeg-python, numpy, sounddevice, pytest, pytest-cov, ruff
- **Domaine** : other (media / transcription audio-video)
- **Date de génération** : 2026-06-13
- **Score de validation** : 85 / 100

## Historique des générations

| Date | Projet | Stack | Score |
|------|--------|-------|-------|
| 2026-06-13 | transcripteur | Python 3.11, Poetry, Typer, Rich, faster-whisper, onnxruntime, torchaudio, ffmpeg-python, numpy, sounddevice, pytest, pytest-cov, ruff | 85 |

## Patterns identifiés

### Stacks fréquemment utilisés
1. Python CLI (Typer + Rich) — projet de transcription audio
2. faster-whisper + onnxruntime — inference locale Whisper

### Erreurs récurrentes
- Modes planifiés (mic, benchmark) non encore implementes → prioriser dans la roadmap
- Pas de CI/CD ni Docker → ajouter `.github/workflows` et `Dockerfile` si besoin de distribuer

## Apprentissages

### Ce qui fonctionne bien
- Structure Poetry propre avec `src/` layout
- CLI modulaire avec sous-commandes (transcribe, doctor, mic, benchmark)
- Tests pytest deja en place (test_cli, test_config)
- Outillage Windsurf deja tres fourni (5 skills + 7 workflows)

### Ce qui peut être amélioré
- Ajouter un fichier CONTRIBUTING.md
- Mettre en place un pipeline CI minimal (lint + tests)
- Completer l'implementation du mode microphone et du benchmark
- Ajouter des regles `.devin/rules/` pour renforcer la qualite du code
