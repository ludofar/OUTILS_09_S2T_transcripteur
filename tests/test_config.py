"""Tests pour la configuration de Transcripteur."""

from __future__ import annotations

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from transcripteur.config import AppConfig, ExportOptions, WhisperOptions


def test_app_config_defaults(tmp_path: Path) -> None:
    config = AppConfig()
    config_path = tmp_path / "config.json"
    config.save(config_path)

    loaded = AppConfig.load(config_path)
    assert loaded.whisper.model_name == "base"
    assert loaded.whisper.device == "cpu"
    assert loaded.export.export_json is True
    assert loaded.export.output_dir == Path("outputs")


def test_app_config_from_dict_override(tmp_path: Path) -> None:
    payload = {
        "whisper": {"model_name": "small", "device": "cpu", "beam_size": 3},
        "export": {"export_text": False, "output_dir": "custom"},
    }
    config_path = tmp_path / "cfg.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")

    config = AppConfig.load(config_path)
    assert config.whisper.model_name == "small"
    assert config.whisper.beam_size == 3
    assert config.export.export_text is False
    assert config.export.output_dir == Path("custom")


def test_app_config_presets_apply(tmp_path: Path) -> None:
    payload = {
        "whisper": {"model_name": "base", "device": "cpu"},
        "export": {"output_dir": "base_outputs"},
        "presets": {
            "fast": {
                "whisper": {"model_name": "tiny"},
                "export": {"output_dir": "fast_outputs"},
            }
        },
        "default_preset": "fast",
    }
    config_path = tmp_path / "cfg_presets.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")

    config = AppConfig.load(config_path)
    assert config.default_preset == "fast"
    assert "fast" in config.presets

    applied = config.apply_preset("fast")
    assert applied is True
    assert config.whisper.model_name == "tiny"
    assert config.export.output_dir == Path("fast_outputs")

    # Un preset inconnu ne doit pas lever d'exception et renvoie False
    assert config.apply_preset("unknown") is False
