from typing import Dict, Any
from .dummy import DummyProvider
try:
    from .openai import OpenAIProvider
except Exception:
    OpenAIProvider = None

def build_provider(cfg: Dict[str, Any]):
    ptype = cfg.get("type", "dummy")
    params = cfg.get("params", {}) or {}
    if ptype == "dummy":
        return DummyProvider(**params)
    if ptype == "openai":
        if OpenAIProvider is None:
            raise RuntimeError("OpenAI provider unavailable.")
        return OpenAIProvider(**params)
    raise KeyError(f"Unknown provider type: {ptype}")
