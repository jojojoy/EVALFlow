# EVALFlow

![CI](https://github.com/jojojoy/EVALFlow/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **EVALFlow** is a lightweight **LLM evaluation & regression monitoring toolkit** in Python.  
> It helps you run reproducible benchmarks, compute metrics, and generate reports (HTML/Markdown) for model comparison.

---

## ✨ Features

- 📊 **Metrics**: ROUGE-L, Accuracy, BLEU (with smoothing)  
- 🤖 **Providers**:
  - DummyProvider (offline demo)
  - OpenAIProvider (`pip install -e .[openai]`, requires `OPENAI_API_KEY`)
- 📑 **Reporters**: HTML + Markdown reports (auto-generated)
- ⚙️ **Config-driven**: run tasks via YAML configs (`configs/`)
- 🔄 **Regression Monitoring**: compare runs against baselines
- ✅ **CI Ready**: tested via GitHub Actions (`pytest`)

---

## 🚀 Quickstart

### 1. Install
```bash
git clone https://github.com/jojojoy/EVALFlow.git
cd EVALFlow
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -e .[dev]

---

## 📊 Example Output

After running:

```bash
evalflow run --config configs/summarization.yaml --out runs/demo