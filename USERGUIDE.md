# Transcripteur — Guide Utilisateur Complet

> Version du guide : 1.0 — Couvre toutes les commandes, options, pipelines et points d'extension de `transcripteur v0.1.0`.

---

## 1. Vue d'ensemble

**Transcripteur** est une interface en ligne de commande (CLI) Python pour transcrire en local des fichiers audio/vidéo en français (ou toute autre langue supportée par Whisper) avec les modèles OpenAI Whisper, via la bibliothèque optimisée `faster-whisper`.

**Architecture du pipeline** (valable pour `transcribe` et `mic`) :

```
Média source
    ↓
[FFmpeg] Extraction audio WAV 16 kHz mono
    ↓
[FFmpeg] Prétraitement (débruitage + normalisation + filtre passe-haut)
    ↓
[faster-whisper] Transcription avec VAD
    ↓
Export (.txt / .json / .srt)
```

**Dépendances clés** :
- `faster-whisper` — inférence Whisper optimisée (CTranslate2)
- `torch` / `torchaudio` — backend deep learning
- `ffmpeg-python` + binaire FFmpeg système — extraction et traitement audio
- `typer` + `rich` — CLI ergonomique avec retour visuel
- `sounddevice` — capture microphone (mode `mic`)

---

## 2. Commandes disponibles

```bash
transcripteur [COMMAND] [OPTIONS]
```

| Commande | Description |
|----------|-------------|
| `doctor` | Diagnostic complet de l'environnement d'exécution |
| `transcribe` | Transcription d'un fichier média avec exports |
| `benchmark` | Mesure des performances des modèles Whisper |
| `mic` | Enregistrement microphone en continu puis transcription (dictée) |
| `version` | Affiche la version du package |

Pour l'aide contextuelle d'une commande :
```bash
transcripteur transcribe --help
```

---

## 3. Commande `doctor` — Diagnostic

**Usage** :
```bash
transcripteur doctor [OPTIONS]
```

**Options** :
- `--model TEXT` — Nom du modèle à charger pour le test (défaut : `tiny`)
- `--skip-whisper` — Ne pas charger Whisper (diagnostic léger)
- `--verbose / -v` — Afficher les détails

**Vérifications effectuées** :
1. Version Python et implémentation (CPython/PyPy)
2. Présence et version de FFmpeg dans le `PATH`
3. Version de PyTorch et disponibilité CUDA
4. Import de `faster-whisper`
5. Chargement d'un modèle Whisper
6. Transcription de test sur un signal muet de 1 seconde

**Cas d'usage** :
- Après installation pour valider que tout fonctionne
- Avant un traitement par lot pour s'assurer que CUDA est bien détecté
- Pour identifier la cause d'un échec de transcription

---

## 4. Commande `transcribe` — Transcription de fichiers

**Usage** :
```bash
transcripteur transcribe CHEMIN_MEDIA [OPTIONS]
```

**Argument obligatoire** :
- `MEDIA` — Chemin du fichier média (vidéo ou audio). Le fichier doit exister et être lisible.

### 4.1 Options de la commande

| Option | Court | Description | Défaut |
|--------|-------|-------------|--------|
| `--config` | `-c` | Chemin vers un fichier de configuration JSON | `transcripteur.json` (dans le répertoire courant) |
| `--output-dir` | `-o` | Répertoire de sortie pour les exports | `outputs` |
| `--model` | | Nom du modèle Whisper (`tiny`, `base`, `small`, `medium`, `large`, `large-v2`, etc.) | `base` |
| `--device` | | Périphérique (`cpu`, `cuda`, `auto`) | `cpu` |
| `--language` | | Code langue ISO (`fr`, `en`, `es`...) | `fr` |
| `--preset` | `-p` | Nom d'un preset de configuration à charger | (aucun) |
| `--sample-rate` | | Fréquence d'échantillonnage cible en Hz | `16000` |
| `--export-text / --no-export-text` | | Activer/désactiver l'export texte | activé |
| `--export-json / --no-export-json` | | Activer/désactiver l'export JSON | activé |
| `--export-srt / --no-export-srt` | | Activer/désactiver l'export SRT | activé |
| `--verbose` | `-v` | Logs détaillés | désactivé |

### 4.2 Pipeline interne détaillé

La commande `transcribe` exécute séquentiellement :

**Étape 1 — Extraction audio**
- FFmpeg extrait la piste audio du média source
- Format WAV PCM, mono, 16 kHz (configurable via `--sample-rate`)
- Le fichier est stocké dans un répertoire temporaire

**Étape 2 — Prétraitement audio** (conditionnel)
- Activé si `denoise=True` ou `normalize=True` dans la configuration
- Filtres FFmpeg appliqués en chaîne :
  - **Filtre passe-haut** (`highpass`) — élimine le ronflement de fond (fréquence configurable, défaut 80 Hz)
  - **Débruitage** (`afftdn`) — réduction adaptative du bruit en domaine fréquentiel
  - **Normalisation** (`loudnorm`) — normalisation au standard EBU R128 (intégré -16 LUFS, True Peak -1.5 dB, LRA 11)

**Étape 3 — Transcription Whisper**
- Chargement du modèle spécifié (lazy loading, mis en cache en mémoire)
- Paramètres d'inférence complète (voir §6)
- Application du filtre VAD (Voice Activity Detection) via Silero pour supprimer les segments de silence

**Étape 4 — Export**
- Les trois formats activés sont générés dans le répertoire de sortie
- Le nom de base des fichiers correspond au nom du média source (sans extension)

### 4.3 Exemples d'usage

**Transcription simple (CPU, modèle base)** :
```bash
transcripteur transcribe ma_video.mp4
```

**Transcription rapide avec modèle léger** :
```bash
transcripteur transcribe podcast.mp3 --model tiny --device cpu
```

**Transcription avec langue anglaise, sans export SRT** :
```bash
transcripteur transcribe interview.wav --language en --no-export-srt
```

**Utilisation d'un preset personnalisé** :
```bash
transcripteur transcribe conference.mkv --preset qualite_max
```

**Personnalisation complète** :
```bash
transcripteur transcribe film.mp4 \
  --model medium \
  --device cuda \
  --language fr \
  --output-dir ./resultats \
  --sample-rate 16000 \
  --verbose
```

---

## 5. Commande `benchmark` — Mesure de performance

**Usage** :
```bash
transcripteur benchmark FICHIER1 [FICHIER2 ...] [OPTIONS]
```

**Arguments** :
- `MEDIA` (un ou plusieurs fichiers) — Échantillons audio/vidéo à utiliser pour le benchmark

**Options** :
- `--models / -m` — Liste des modèles à tester, séparés par des virgules (défaut : `tiny,base`)
- `--device` — Périphérique (`cpu`, `cuda`) (défaut : `cpu`)
- `--language` — Langue forcée (défaut : celle de la config)
- `--sample-rate` — Fréquence d'échantillonnage (défaut : `16000`)
- `--output-json` — Chemin du fichier de résultats (défaut : `outputs/benchmark.json`)
- `--verbose / -v` — Logs détaillés

### 5.1 Fonctionnement

Pour chaque modèle demandé :
1. Extraction audio de tous les médias fournis
2. Transcription de chaque média
3. Mesure du temps écoulé (wall-clock time)
4. Calcul du ratio `temps_de_traitement / duree_audio`
5. Écriture des résultats au format JSON structuré

**Structure du JSON de sortie** :
```json
{
  "media": [
    {"path": "sample.mp3", "duration_seconds": 30.0}
  ],
  "device": "cpu",
  "language": "fr",
  "results": [
    {
      "model": "tiny",
      "device": "cpu",
      "language": "fr",
      "wall_time_sec": 5.23,
      "audio_seconds": 30.0,
      "sec_per_audio_second": 0.174,
      "success": true,
      "error": null
    }
  ]
}
```

### 5.2 Cas d'usage

- **Choisir le bon modèle** pour sa machine avant un traitement par lot
- **Comparer CPU vs CUDA** en exécutant deux benchmarks
- **Alimenter la sélection automatique** du mode `mic` (voir §7)

**Exemple** :
```bash
transcripteur benchmark sample_30s.mp3 --models tiny,base,small -m --device cpu --output-json outputs/bench_cpu.json
```

---

## 6. Commande `mic` — Dictée par microphone

**Usage** :
```bash
transcripteur mic [OPTIONS]
```

**Options** :
- `--config / -c` — Fichier de configuration JSON
- `--model` — Nom du modèle ou `auto` (défaut : `auto`)
- `--device` — `cpu`, `cuda` ou `auto` (défaut : `auto`)
- `--language` — Code langue (défaut : `fr`)
- `--preset / -p` — Preset de configuration
- `--sample-rate` — Fréquence d'échantillonnage micro (défaut : `16000`)
- `--max-seconds` — Durée maximale d'enregistrement (Ctrl+C pour arrêter plus tôt)
- `--output / -o` — Fichier texte de sortie
- `--timestamps` — Afficher les horodatages dans la sortie
- `--save-wav` — Chemin du fichier WAV capturé
- `--verbose / -v` — Logs détaillés

### 6.1 Sélection automatique du modèle (`auto`)

Si `--model auto` est spécifié, le système :
1. Lit les résultats de benchmark existants (`outputs/benchmark.json` ou `outputs/benchmark_youtube_30s.json`)
2. Préfère le modèle `small` s'il est disponible et performant
3. Sinon sélectionne le modèle avec le meilleur ratio `sec_per_audio_second`
4. Si aucun benchmark n'existe, utilise `small` par défaut

### 6.2 Pipeline interne

**Phase 1 — Enregistrement**
- Capture du microphone via `sounddevice` (PortAudio)
- Blocs de 0,5 seconde lus en continu
- Écriture simultanée dans un fichier WAV (streaming)
- Affichage d'un compteur temps réel `MM:SS`
- Arrêt par Ctrl+C ou par dépassement de `--max-seconds`

**Phase 2 — Prétraitement**
- Application conditionnelle des filtres de débruitage et normalisation

**Phase 3 — Transcription**
- Transcription du WAV (original ou prétraité)
- Affichage du ratio de vitesse (temps de transcription / durée audio)

**Phase 4 — Export**
- Affichage dans la console (avec ou sans timestamps)
- Écriture dans le fichier texte spécifié (défaut : `outputs/mic_YYYYMMDD_HHMMSS.txt`)

### 6.3 Exemples d'usage

**Dictée simple** (Ctrl+C pour arrêter) :
```bash
transcripteur mic
```

**Dictée limitée à 60 secondes avec timestamps** :
```bash
transcripteur mic --max-seconds 60 --timestamps
```

**Dictée avec modèle explicite et sortie personnalisée** :
```bash
transcripteur mic --model base --device cpu --output ma_note.txt --save-wav ma_voix.wav
```

---

## 7. Système de configuration

Le fichier de configuration par défaut est `transcripteur.json` dans le répertoire de travail. Il peut être spécifié explicitement via `--config`.

### 7.1 Structure du fichier JSON

```json
{
  "whisper": {
    "model_name": "base",
    "device": "cpu",
    "language": "fr",
    "beam_size": 5,
    "temperature": 0.0,
    "best_of": 5,
    "patience": 1.0,
    "condition_on_previous_text": true,
    "compression_ratio_threshold": 2.4,
    "logprob_threshold": -1.0,
    "no_speech_threshold": 0.6,
    "vad_filter": true,
    "vad_threshold": 0.5,
    "vad_min_silence_duration_ms": 500,
    "vad_speech_pad_ms": 200,
    "denoise": true,
    "normalize": true,
    "highpass_freq": 80
  },
  "export": {
    "export_text": true,
    "export_json": true,
    "export_srt": true,
    "output_dir": "outputs"
  },
  "presets": {
    "qualite_max": {
      "whisper": {
        "model_name": "large",
        "beam_size": 10,
        "temperature": 0.0,
        "vad_filter": true
      },
      "export": {
        "export_text": true,
        "export_json": true,
        "export_srt": true
      }
    },
    "rapide": {
      "whisper": {
        "model_name": "tiny",
        "beam_size": 1,
        "temperature": 0.0,
        "vad_filter": false
      },
    }
  },
  "default_preset": null
}
```

### 7.2 Options Whisper détaillées

| Option | Description | Valeur par défaut |
|--------|-------------|-------------------|
| `model_name` | Taille du modèle Whisper | `base` |
| `device` | Périphérique (`cpu`, `cuda`) | `cpu` |
| `language` | Langue forcée (`fr`, `en`...) | `fr` |
| `beam_size` | Taille du faisceau de recherche | `5` |
| `temperature` | Température d'échantillonnage (0 = déterministe) | `0.0` |
| `best_of` | Nombre de candidats générés par échantillonnage | `5` |
| `patience` | Patience pour la recherche en faisceau | `1.0` |
| `condition_on_previous_text` | Conditionner sur le texte précédent | `true` |
| `compression_ratio_threshold` | Seuil de rejet par ratio de compression | `2.4` |
| `logprob_threshold` | Seuil de rejet par log-probabilité | `-1.0` |
| `no_speech_threshold` | Seuil de détection de non-parole | `0.6` |
| `vad_filter` | Activer le filtre VAD Silero | `true` |
| `vad_threshold` | Seuil de détection VAD | `0.5` |
| `vad_min_silence_duration_ms` | Durée minimale de silence pour couper (ms) | `500` |
| `vad_speech_pad_ms` | Padding autour des segments de parole (ms) | `200` |
| `denoise` | Activer le débruitage FFmpeg | `true` |
| `normalize` | Activer la normalisation EBU R128 | `true` |
| `highpass_freq` | Fréquence de coupure du filtre passe-haut (Hz) | `80` |

### 7.3 Presets

Les presets permettent de définir des configurations nommées réutilisables. Un preset modifie uniquement les champs qu'il définit ; les autres conservent leurs valeurs par défaut.

**Appliquer un preset** :
```bash
transcripteur transcribe film.mp4 --preset qualite_max
transcripteur mic --preset rapide
```

**Définir un preset par défaut** :
```json
{
  "default_preset": "rapide",
  ...
}
```

---

## 8. Formats d'export

### 8.1 Texte brut (`.txt`)
- Une ligne par segment de transcription
- Pas d'horodatage
- Texte nettoyé (strip des espaces superflus)

### 8.2 JSON (`.json`)
Structure complète incluant :
- `language` — Langue détectée
- `segments` — Tableau d'objets `{start, end, text}`
- `raw` — Données brutes de `faster-whisper` (probabilités de langue, durée post-VAD, etc.)

### 8.3 SRT (`.srt`)
Format standard de sous-titres :
```srt
1
00:00:01,234 --> 00:00:04,567
Bonjour et bienvenue dans cette vidéo.

2
00:00:04,890 --> 00:00:07,123
Aujourd'hui nous allons parler de...
```

---

## 9. Prétraitement audio (FFmpeg)

Le module `preprocessing.py` expose deux fonctions utilisées par les commandes `transcribe` et `mic`.

### 9.1 Extraction audio (`extract_audio`)

Convertit n'importe quel format supporté par FFmpeg en WAV PCM mono 16 kHz.

**Paramètres internes** :
- `sample_rate` — 16000 Hz (optimal pour Whisper)
- `channels` — 1 (mono)
- `overwrite` — Écrase les fichiers existants

### 9.2 Débruitage et normalisation (`denoise_and_normalize_audio`)

Chaîne de filtres FFmpeg appliquée en un seul passage :

1. **Filtre passe-haut** (`highpass=f=80`) — Supprime les fréquences infrasonores (ronflement, ventilateurs)
2. **Débruitage** (`afftdn=nf=-20:nr=0.8:tn=1`) — Réduction adaptative du bruit par analyse spectrale
3. **Normalisation** (`loudnorm=I=-16:TP=-1.5:LRA=11`) — Normalisation au standard EBU R128

Ces traitements améliorent significativement la qualité de transcription sur des enregistrements bruyants ou de niveau inégal.

---

## 10. Utilisation programmatique (API Python)

Bien que principalement conçu comme CLI, Transcripteur peut être utilisé depuis du code Python.

### 10.1 Transcription d'un fichier

```python
from pathlib import Path
from transcripteur.config import AppConfig, WhisperOptions
from transcripteur.transcription import WhisperTranscriber
from transcripteur.export import export_all

# Configuration
options = WhisperOptions(
    model_name="base",
    device="cpu",
    language="fr",
    vad_filter=True,
)

# Transcription
transcriber = WhisperTranscriber(options)
result = transcriber.transcribe_file(Path("mon_audio.wav"))

# Export
for path in export_all(result, Path("sorties"), "mon_audio"):
    print(f"Exporté : {path}")
```

### 10.2 Transcription d'un array NumPy

```python
import numpy as np
from transcripteur.transcription import WhisperTranscriber
from transcripteur.config import WhisperOptions

options = WhisperOptions(model_name="tiny", device="cpu")
transcriber = WhisperTranscriber(options)

# Audio déjà en mémoire (float32, 16 kHz, mono)
audio = np.random.randn(16000).astype(np.float32)  # 1 seconde
transcriber.transcribe_array(audio)
```

### 10.3 Chargement d'une configuration

```python
from transcripteur.config import AppConfig

# Charge transcripteur.json dans le répertoire courant
config = AppConfig.load()

# Ou depuis un chemin explicite
config = AppConfig.load(Path("config_prod.json"))

# Appliquer un preset
config.apply_preset("qualite_max")

# Sauvegarder
config.save(Path("ma_config.json"))
```

---

## 11. Modèles Whisper disponibles

Les modèles supportés par `faster-whisper` (et donc par Transcripteur) :

| Modèle | Paramètres | Usage recommandé | Qualité |
|--------|------------|------------------|---------|
| `tiny` | 39 M | Tests rapides, machines lentes | Faible |
| `base` | 74 M | Premier essai, transcription rapide | Moyenne |
| `small` | 244 M | Équilibre qualité/vitesse | Bonne |
| `medium` | 769 M | Qualité élevée, machines modernes | Très bonne |
| `large` | 1550 M | Qualité maximale, GPU recommandé | Excellente |
| `large-v2` / `large-v3` | 1550 M | Dernières versions optimisées | Excellente |

**Règles empiriques** :
- CPU uniquement : `tiny` à `small`
- GPU modeste : `medium`
- GPU performant : `large`

---

## 12. Conseils et bonnes pratiques

### 12.1 Choix du modèle

Exécutez un benchmark sur un échantillon représentatif avant un traitement par lot :
```bash
transcripteur benchmark echantillon.mp3 --models tiny,base,small,medium --device cpu
```

### 12.2 Qualité de transcription

- Activez `denoise` et `normalize` pour des sources bruyantes (micro, conférences)
- Utilisez le filtre VAD pour éliminer les longs silences
- Le filtre passe-haut à 80 Hz est utile pour les enregistrements avec ronflement de fond
- Augmentez `beam_size` (8-10) pour plus de précision au détriment de la vitesse

### 12.3 Performance

- Sur CPU, préférez les modèles `tiny` et `base`
- Si CUDA est disponible, `--device cuda` accélère drastiquement `medium` et `large`
- Le prétraitement FFmpeg est rapide comparé à l'inférence Whisper

### 12.4 Traitement par lot

Pour traiter plusieurs fichiers, utilisez une boucle shell ou un script :

```bash
for f in videos/*.mp4; do
  transcripteur transcribe "$f" --model small --output-dir resultats/
done
```

---

## 13. Messages d'erreur courants

| Symptôme | Cause probable | Solution |
|----------|---------------|----------|
| `FFmpeg introuvable` | FFmpeg non dans le PATH | Installer FFmpeg et l'ajouter au PATH système |
| `FFmpegError` | Fichier média corrompu ou format non supporté | Vérifier le fichier avec `ffprobe` |
| `No module named transcripteur` | Package non installé | `pip install -e .` depuis la racine du projet |
| Échec VAD | `sounddevice` ou PortAudio manquant (mode `mic`) | Installer PortAudio système et réinstaller `sounddevice` |
| CUDA non disponible | PyTorch CPU installé | Installer PyTorch avec support CUDA |

---

## 14. Fichiers générés

| Fichier | Description |
|---------|-------------|
| `outputs/<media>.txt` | Transcription texte brute |
| `outputs/<media>.json` | Transcription structurée avec métadonnées |
| `outputs/<media>.srt` | Sous-titres synchronisés |
| `outputs/benchmark.json` | Résultats des benchmarks |
| `outputs/mic_YYYYMMDD_HHMMSS.wav` | Audio capturé par le micro |
| `outputs/mic_YYYYMMDD_HHMMSS.txt` | Transcription du mode micro |
| `transcripteur.json` | Fichier de configuration utilisateur |

---

## 15. Schéma récapitulatif des fonctionnalités

```
┌─────────────────────────────────────────────────────────────┐
│                    TRANSCRIPTEUR v0.1.0                     │
├─────────────────────────────────────────────────────────────┤
│  COMMANDS                                                   │
│  ├── doctor      → Diagnostic environnement (Python, FFmpeg,│
│  │                 PyTorch, faster-whisper, modèle test)    │
│  ├── transcribe  → Extraction → Prétraitement → Whisper →   │
│  │                 Export (.txt/.json/.srt)                  │
│  ├── benchmark   → Mesure performance modèles Whisper        │
│  ├── mic         → Capture micro → Prétraitement → Whisper  │
│  │                 → Texte (avec timestamps optionnels)      │
│  └── version     → Numéro de version                       │
├─────────────────────────────────────────────────────────────┤
│  AUDIO PIPELINE                                             │
│  • Extraction FFmpeg (WAV 16kHz mono)                     │
│  • Filtre passe-haut configurable                           │
│  • Débruitage spectral (afftdn)                             │
│  • Normalisation EBU R128 (loudnorm)                        │
├─────────────────────────────────────────────────────────────┤
│  WHISPER OPTIONS                                            │
│  • Modèles : tiny → large-v3                                │
│  • Device : cpu / cuda / auto                               │
│  • Langue forcée ou auto-détectée                           │
│  • Beam search, temperature, best_of                        │
│  • VAD Silero avec seuils configurables                   │
├─────────────────────────────────────────────────────────────┤
│  CONFIGURATION                                              │
│  • Fichier JSON `transcripteur.json`                        │
│  • Presets nommés réutilisables                             │
│  • Héritage : défaut → fichier → preset → CLI             │
├─────────────────────────────────────────────────────────────┤
│  EXPORTS                                                    │
│  • Texte brut (.txt)                                        │
│  • JSON structuré avec métadonnées (.json)                  │
│  • Sous-titres SRT (.srt)                                   │
└─────────────────────────────────────────────────────────────┘
```

---

*Guide généré le 14 juin 2026. Pour toute évolution du code, exécutez `transcripteur --help` ou consultez les docstrings du package.*
