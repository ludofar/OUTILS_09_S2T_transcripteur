---
name: s2t-transcribe
description: Lance une transcription Speech-to-Text (faster-whisper) sur un fichier audio/video en local. Genere des exports .txt, .json et .srt avec horodatages.
argument-hint: "<chemin_fichier_media> [--model tiny|base|small|medium] [-o dossier_sortie]"
allowed-tools:
  - read
  - glob
  - exec
permissions:
  allow:
    - Exec(powershell)
    - Exec(.\transcribe.ps1)
    - Read(.venv/**)
    - Read(src/**)
    - Read(transcripteur.json)
    - Read(outputs/**)
---

# Skill : Transcription Speech-to-Text (S2T)

Tu es un assistant specialise dans le lancement de transcriptions audio/vidéo en local via le CLI `transcripteur` du projet `OUTILS_09_S2T_transcripteur`. Ce projet utilise **faster-whisper** (moteur CTranslate2) avec FFmpeg pour le pretraitement.

## Contexte projet

- **Racine projet** : `C:\BOULOT\TRAVAIL avec windsurf\OUTILS_09_S2T_transcripteur`
- **Venv Python** : `.venv\Scripts\python.exe` (Python 3.12.10)
- **Script de lancement** : `transcribe.ps1` (a la racine du projet) — preconfigure PATH FFmpeg et PYTHONPATH automatiquement
- **Config par defaut** : `transcripteur.json` (modele `small`, langue `fr`, device `cpu`)
- **Dossier d'export par defaut** : `outputs/`

## Procedure a suivre

### 1. Identifier le fichier a transcrire

L'utilisateur fournit le chemin du fichier media en argument du skill, ou le mentionne dans sa demande. Si aucun fichier n'est fourni, demande-le explicitement.

Formats supportes (via FFmpeg) : `.mp4`, `.mkv`, `.avi`, `.mov`, `.mp3`, `.wav`, `.m4a`, `.flac`, `.aac`, `.ogg`, `.webm`, etc.

**Important** : Verifie que le fichier existe avec `Test-Path` avant de lancer la transcription. Si le chemin contient des espaces, entoure-le de guillemets.

### 2. Verifier l'environnement (premier lancement uniquement)

Si tu n'es pas sur que l'environnement est operationnel, lance d'abord :

```powershell
cd "C:\BOULOT\TRAVAIL avec windsurf\OUTILS_09_S2T_transcripteur"; .\transcribe.ps1 doctor --model tiny --skip-whisper
```

Doit afficher : Python 3.12.x, FFmpeg present, PyTorch charge. Si le venv est cassé ou FFmpeg absent, arrete-toi et signale-le a l'utilisateur (voir section "Troubleshooting" ci-dessous).

### 3. Lancer la transcription

Place-toi dans le dossier du projet et lance le script `transcribe.ps1` avec les arguments appropries :

```powershell
cd "C:\BOULOT\TRAVAIL avec windsurf\OUTILS_09_S2T_transcripteur"
.\transcribe.ps1 transcribe "<chemin_fichier>" [options]
```

#### Options disponibles

| Option | Defaut | Description |
|---|---|---|
| `--model` | `small` (via config) | `tiny` (~75 Mo, rapide), `base` (~145 Mo), `small` (~480 Mo, bon compromis), `medium` (~1.5 Go, lent sur CPU), `large-v3` (~3 Go, GPU conseille) |
| `--device` | `cpu` | `cpu` ou `cuda` (si GPU NVIDIA avec CUDA) |
| `--language` | `fr` | Code langue ISO (ex: `fr`, `en`, `es`, `de`) |
| `-o` / `--output-dir` | `outputs` | Dossier des exports |
| `--export-text` / `--no-export-text` | active | Export `.txt` (transcription continue) |
| `--export-json` / `--no-export-json` | active | Export `.json` (segments + horodatages + metadonnees) |
| `--export-srt` / `--no-export-srt` | active | Export `.srt` (sous-titres synchronises) |
| `--verbose` / `-v` | non | Affiche les logs detailles |
| `--config` / `-c` | `transcripteur.json` | Fichier de config alternatif |
| `--preset` / `-p` | aucun | Nom d'un preset defini dans la config |

#### Choix du modele — guide de decision

- **Test rapide / fichier court (< 1 min)** : `--model tiny`
- **Usage standard en francais (recommande)** : `--model small` (defaut)
- **Qualite maximale, fichier long, CPU puissant** : `--model medium`
- **GPU NVIDIA disponible** : `--model medium` ou `large-v3` avec `--device cuda`

#### Exemples concrets

```powershell
# Transcription standard (modele small par defaut, sortie dans outputs/)
.\transcribe.ps1 transcribe "C:\chemin\vers\reunion.mp4"

# Transcription rapide avec modele tiny
.\transcribe.ps1 transcribe "C:\chemin\vers\audio.mp3" --model tiny

# Transcription avec dossier de sortie personnalise
.\transcribe.ps1 transcribe "D:\videos\interview.mkv" -o ".\sorties_interview"

# Transcription en anglais
.\transcribe.ps1 transcribe "C:\podcast.wav" --language en --model small

# Transcription sans pretraitement (audio deja propre)
.\transcribe.ps1 transcribe "C:\audio_propre.wav" --model small --verbose
```

### 4. Attendre la transcription

La transcription peut etre longue. Sur CPU avec le modele `small`, compte environ **2-4x la duree du media** :
- 10 min de video -> 20-40 min de transcription
- 1 h de video -> 2-4 h de transcription

**Premier lancement d'un modele** : le modele est telecharge depuis HuggingFace et mis en cache dans `~/.cache/huggingface/`. Cela ajoute quelques minutes la premiere fois (selon la taille du modele et le debit reseau).

Utilise `timeout: 0` (background) pour les longues transcriptions, et verifie la sortie avec `get_output`.

### 5. Reporter le resultat a l'utilisateur

Une fois la transcription terminee, verifie que les fichiers d'export ont bien ete crees dans le dossier de sortie. Pour un media `mon_fichier.mp4`, tu dois trouver :

- `mon_fichier.txt` — transcription continue (texte brut)
- `mon_fichier.json` — segments avec `start`, `end`, `text` + metadonnees (langue, duree, probabilite)
- `mon_fichier.srt` — sous-titres synchronises

**Signale a l'utilisateur** :
1. Le chemin absolu des fichiers generes
2. La langue detectee et la duree du media (lisible dans le JSON)
3. Le nombre de segments transcrits
4. Tout warning eventuel (ex: segments vides si audio sans parole)

Exemple de rapport :
> Transcription terminee. 3 fichiers generes dans `outputs/` :
> - `interview.txt` (texte brut)
> - `interview.json` (47 segments, langue fr, duree 12:34)
> - `interview.srt` (sous-titres)

## Architecture du pipeline (pour comprendre ce qui se passe)

La commande `transcribe` execute 3 etapes (voir `src/transcripteur/commands/transcribe.py`) :

1. **Extraction audio** (FFmpeg) : convertit le media en WAV 16 kHz mono
2. **Pretraitement** (FFmpeg) : denoisage (afftdn) + normalisation EBU R128 + filtre passe-haut 80 Hz
3. **Transcription** (faster-whisper) : VAD Silero + transcription avec beam search
4. **Exports** : generation des fichiers `.txt`, `.json`, `.srt`

Le pretraitement est active par defaut (`denoise: true`, `normalize: true` dans la config). Pour le desactiver, modifie `transcripteur.json` ou cree un preset.

## Troubleshooting

### "No Python at..." / venv casse
Le fichier `.venv\pyvenv.cfg` pointe vers un Python qui n'existe plus. Recree le venv :
```powershell
$py = "C:\Users\ludof\AppData\Local\Programs\Python\Python312\python.exe"
Remove-Item ".venv" -Recurse -Force
& $py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### "FFmpeg introuvable dans le PATH"
Le script `transcribe.ps1` cherche automatiquement FFmpeg dans le cache winget. Si FFmpeg n'est pas installe :
```powershell
winget install --id Gyan.FFmpeg --source winget --accept-package-agreements
```
Puis relance la transcription.

### "CUDA disponible : False" (alors qu'on a un GPU NVIDIA)
PyTorch a ete installe en version CPU-only. Pour activer CUDA, il faut installer la version GPU de torch :
```powershell
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cu121
```
Puis utiliser `--device cuda`.

### Transcription vide (0 segment)
Causes possibles :
- Le fichier audio ne contient pas de parole (musique, silence)
- Le VAD (Voice Activity Detection) a filtre tout le contenu — essaie avec `--verbose` ou desactive le VAD en modifiant `transcripteur.json` (`vad_filter: false`)
- Le fichier est corrompu — verifie avec `ffmpeg -i <fichier>`

### `--help` n'affiche rien
Bug d'affichage connu (compat Typer 0.27 / Rich 15). Les options fonctionnent toutes — refere-toi au tableau ci-dessus.

### Modele qui met tres longtemps a se charger (premier lancement)
Normal : faster-whisper telecharge le modele depuis HuggingFace au premier appel, puis le met en cache. Les lancements suivants sont instantanes.

## Fichiers cles du projet (pour reference)

- `src/transcripteur/cli.py` — point d'entree CLI (Typer)
- `src/transcripteur/commands/transcribe.py` — commande de transcription
- `src/transcripteur/commands/doctor.py` — diagnostic environnement
- `src/transcripteur/transcription.py` — wrapper faster-whisper
- `src/transcripteur/preprocessing.py` — extraction + pretraitement FFmpeg
- `src/transcripteur/export.py` — exports .txt/.json/.srt
- `src/transcripteur/config.py` — gestion config + presets
- `transcripteur.json` — configuration par defaut (modele, langue, exports)
- `transcribe.ps1` — script de lancement Windows (preconfigure PATH et PYTHONPATH)
- `requirements.txt` — dependances Python
- `docs/prerequis.md` — prerequis materiels et logiciels
- `docs/architecture_overview.md` — architecture detaillee
- `docs/roadmap.md` — feuille de route (mode mic, benchmark, etc.)
