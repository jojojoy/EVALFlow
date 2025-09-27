# EVALFlow

A lightweight, reproducible evaluation pipeline for LLMs with golden datasets and regression/drift monitoring.

## Quickstart

```bash
# From the project root
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -e .
evalflow run --config configs/summarization.yaml --out runs/first-run
# Open the generated HTML report in runs/first-run/report.html
```

## Features
- Reproducible YAML configs and deterministic seeds
- Golden-set regression report (HTML & Markdown)
- Plug-in metrics (ROUGE-L-ish, accuracy), extensible registry
- Providers: `dummy` (no API needed), easy to extend to OpenAI/HF/local REST
- Minimal dependencies; works fully offline with included toy dataset

## Config Schema (example)
```yaml
task: summarization
dataset:
  path: examples/data/summarization_small.jsonl   # local jsonl with fields: input, reference
provider:
  type: dummy
  params:
    strategy: head-words         # head-words|truncate-characters
    max_tokens: 60
metrics: [rougeL]
report:
  type: html
  baseline_run: null             # set to a previous runs/<run>/metrics.json to diff
seed: 123
```

## Extend
- Add a new metric: drop a file under `evalflow/metrics/` and register it in `registry.py`.
- Add a provider: implement `.generate(batch)` in `evalflow/providers/*` and hook it in `factory.py`.

## Tests
```bash
pytest -q
```

## Roadmap
- Add BLEU/chrF, pass@k, toxicity/offensiveness probes
- Add OpenAI/HF providers (placeholders exist; you can wire your keys)


**Repo:** https://github.com/jojojoy/EVALFlow
