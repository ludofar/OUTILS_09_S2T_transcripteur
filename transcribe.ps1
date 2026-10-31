# Script de lancement pour Transcripteur (Windows / PowerShell)
# Usage :
#   .\transcribe.ps1 doctor
#   .\transcribe.ps1 transcribe "C:\chemin\vers\fichier.mp4" -o sorties
#   .\transcribe.ps1 transcribe "C:\chemin\vers\fichier.mp3" --model tiny
#
# Préconfigure automatiquement :
#   - PYTHONPATH = src
#   - PATH += binaire FFmpeg (installé via winget Gyan.FFmpeg)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

# Python du venv
$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $PythonExe)) {
    Write-Host "Erreur : venv introuvable. Lancez d'abord :" -ForegroundColor Red
    Write-Host "  python -m venv .venv && .venv\Scripts\python.exe -m pip install -r requirements.txt"
    exit 1
}

# FFmpeg (recherche dans le cache winget si pas deja dans le PATH)
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    $ffCandidates = Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages" -Filter "ffmpeg.exe" -Recurse -ErrorAction SilentlyContinue
    if ($ffCandidates) {
        $ffBin = Split-Path -Parent $ffCandidates[0].FullName
        $env:PATH = "$ffBin;$env:PATH"
    } else {
        Write-Host "Attention : FFmpeg introuvable dans le PATH." -ForegroundColor Yellow
        Write-Host "Installe-le : winget install --id Gyan.FFmpeg"
    }
}

# PYTHONPATH vers src
$env:PYTHONPATH = Join-Path $ProjectRoot "src"
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

# Transmet tous les arguments a la CLI transcripteur
& $PythonExe -m transcripteur @args
