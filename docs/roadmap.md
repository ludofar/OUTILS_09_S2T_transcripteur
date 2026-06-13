# Feuille de route

## Phase 0 – Mise en place du projet (Semaine 1)
- ✅ Définir le périmètre, les indicateurs de réussite et la documentation.
- ✅ Établir la structure du dépôt, les standards de code et la base outillage.
- ✅ Vérifier les prérequis matériels/logiciels (GPU disponible, installation de FFmpeg, commande `doctor`).

## Phase 1 – Pipeline de transcription cœur (Semaines 2-4)
- ✅ Structurer la CLI (`transcripteur.cli`) : commandes `transcribe`, `doctor`, gestion des logs (`Rich`) et options communes.
- ✅ Implémenter le chargement de configuration (`AppConfig`) et les defaults.
- ✅ Intégrer un module de prétraitement (extraction audio via FFmpeg) et un transcripteur Whisper fonctionnel.
- ✅ Créer les exports basiques (texte/JSON/SRT) avec timeline.
- ✅ Écrire des tests unitaires d’amorçage (CLI, configuration) et valider le pipeline.
 
## Phase 2 – Export et UX (Semaines 5-6)
- ✅ Export SRT implémenté (formatage basique des segments).
- ✅ Mettre en place indicateurs de progression, journalisation et gestion d’erreurs dans le CLI.
- ✅ Introduire la persistance de configuration et la gestion de presets (`AppConfig.presets`, option `--preset`).
- ✅ Étendre les tests d’intégration avec des médias représentatifs (tests automatisés avec stub + test manuel sur `youtube_30s.wav`).

## Phase 3 – Tests d’environnement et préparation du mode `mic` (Semaines 7-8)
- Définir une batterie de tests pour profiler l’environnement de la machine (CPU/GPU, RAM, système) et les contraintes spécifiques au mode dictée.
- Étendre la commande `doctor` ou introduire une commande dédiée (par exemple `benchmark`) pour :
  - tester plusieurs modèles Whisper (`tiny`, `base`, `small`, etc.) sur un corpus d’échantillons audio représentatifs ;
  - mesurer le temps de transcription, la latence et l’utilisation des ressources.
- Générer un rapport de recommandations :
  - proposer un modèle par défaut optimisé pour le mode `mic` (latence / temps quasi réel) ;
  - documenter les profils « qualité » vs « rapidité » et la façon de les surcharger via la configuration.
- Spécifier le comportement attendu de la future commande `mic` :
  - utilisation du modèle recommandé par défaut en fonction des tests ;
  - surcharge possible via les options CLI et la configuration (`AppConfig`).

## Phase 4 – Performance et fiabilité (Semaines 9-10)
- Optimiser le découpage, le batching et l’utilisation GPU.
- Implémenter la reprise de jobs et le traitement par lot.
- Ajouter des hooks de télémétrie (métriques locales) et des benchmarks de performance.
- Réaliser des tests d’acceptation utilisateur avec un panel pilote.

## Phase 5 – Préparation à la release (Semaines 11-12)
- Packager le CLI pour distribution (PyPI, Homebrew tap en option).
- Finaliser la documentation : guide utilisateur, dépannage, référence API.
- Mettre en place la CI/CD avec linting, tests et automatisation des releases.
- Tenir une revue de préparation au lancement et finaliser le plan de release.

## En continu
- Collecter les retours, trier les issues et planifier des améliorations itératives.
- Explorer des fonctionnalités avancées (diarisation, traduction) après le lancement.
