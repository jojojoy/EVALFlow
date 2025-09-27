from pathlib import Path
import json, subprocess, sys

def test_smoke_run(tmp_path):
    # Copy config into tmp dir
    proj = Path(__file__).resolve().parents[1]
    cfg = proj / "configs" / "summarization.yaml"
    out = tmp_path / "run1"
    cmd = [sys.executable, "-m", "evalflow.cli", "run", "--config", str(cfg), "--out", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert (out / "metrics.json").exists()
    with open(out / "metrics.json","r",encoding="utf-8") as f:
        metrics = json.load(f)
    assert "rougeL" in metrics
    assert (out / "report.html").exists()
