"""Fusionner deux fichiers SRT en un seul .md avec balises [J]/[L] par timestamp."""

import re
import sys
from pathlib import Path


def parse_srt(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as f:
        content = f.read()
    blocks = re.split(r"\n\d+\n", content.strip())
    segments = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 2:
            continue
        ts_match = re.match(
            r"(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})", lines[0]
        )
        if not ts_match:
            continue
        start_str = ts_match.group(1)
        end_str = ts_match.group(2)
        text = " ".join(lines[1:]).strip()
        h, m, s = start_str.replace(",", ".").split(":")
        start_sec = float(h) * 3600 + float(m) * 60 + float(s)
        segments.append(
            {"start": start_sec, "start_str": start_str, "end_str": end_str, "text": text}
        )
    return segments


def merge_srt(srt1: Path, srt2: Path, speaker1: str, speaker2: str, output: Path) -> None:
    segs1 = parse_srt(srt1)
    segs2 = parse_srt(srt2)

    merged = []
    for s in segs1:
        merged.append((s["start"], speaker1, s["start_str"], s["end_str"], s["text"]))
    for s in segs2:
        merged.append((s["start"], speaker2, s["start_str"], s["end_str"], s["text"]))
    merged.sort(key=lambda x: x[0])

    with output.open("w", encoding="utf-8") as f:
        f.write(f"# Transcript fusionne — {output.stem}\n\n")
        f.write(f"> Piste 1 ({srt1.stem}) = {speaker1}\n")
        f.write(f"> Piste 2 ({srt2.stem}) = {speaker2}\n")
        f.write("> Fusion par timestamp de debut de segment\n\n---\n\n")
        for _, speaker, start, end, text in merged:
            f.write(f"{speaker} ({start} --> {end})\n{text}\n\n")

    print(f"Fusion: {len(merged)} segments -> {output}")


if __name__ == "__main__":
    base = Path(r"f:\BOULOT\TRAVAIL avec windsurf\Livre_Ju_Lu\Transcripts\260619_matin\transcriptions")
    merge_srt(
        srt1=base / "1-ludofar_.srt",
        srt2=base / "2-y0iki.srt",
        speaker1="[L]",
        speaker2="[J]",
        output=base / "fusion_260619_matin.md",
    )
