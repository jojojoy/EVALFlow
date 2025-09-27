from dataclasses import dataclass
from typing import List, Dict, Any
from pathlib import Path
from ..datasets.loader import load_dataset_from_jsonl
from ..providers.factory import build_provider
from ..metrics.registry import compute
from ..utils.io import ensure_dir, write_json, write_text, load_baseline_metrics
from ..reporters.html import render_html
import yaml
import random
import numpy as np

@dataclass
class EvalConfig:
    task: str
    dataset_path: str
    provider_cfg: Dict[str, Any]
    metrics: List[str]
    report_type: str
    baseline_run: str
    seed: int = 123

def load_config(path: str) -> EvalConfig:
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return EvalConfig(
        task=cfg.get("task", "summarization"),
        dataset_path=cfg["dataset"]["path"],
        provider_cfg=cfg.get("provider", {"type":"dummy", "params":{}}),
        metrics=cfg.get("metrics", ["rougeL"]),
        report_type=cfg.get("report", {}).get("type", "html"),
        baseline_run=cfg.get("report", {}).get("baseline_run"),
        seed=cfg.get("seed", 123),
    )

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)

def run(config_path: str, out_dir: str):
    cfg = load_config(config_path)
    set_seed(cfg.seed)

    out = ensure_dir(out_dir)
    data = load_dataset_from_jsonl(cfg.dataset_path)
    provider = build_provider(cfg.provider_cfg)

    # Generate predictions
    batch = [{"input": ex["input"]} for ex in data]
    preds = provider.generate(batch)
    refs = [ex["reference"] for ex in data]

    # Compute metrics
    agg = compute(cfg.metrics, preds, refs)

    # Persist artifacts
    rows = []
    for ex, p in zip(data, preds):
        rows.append({
            "input": ex["input"],
            "prediction": p,
            "reference": ex["reference"]
        })

    write_json(out / "predictions.json", rows)
    write_json(out / "metrics.json", agg)

    # Baseline (optional)
    baseline = load_baseline_metrics(cfg.baseline_run)

    # Reports
    if cfg.report_type == "html":
        render_html(out, rows, agg, baseline_aggregate=baseline)
    # also dump md summary
    md = "# Metrics\n" + "\n".join(f"- **{k}**: {v:.4f}" for k, v in agg.items())
    write_text(out / "report.md", md)

    return {"metrics": agg, "out_dir": str(out)}
