from typing import List, Dict, Any
from .base import BaseProvider

class DummyProvider(BaseProvider):
    """A simple offline provider for demos.
    - strategy=head-words: return first N tokens of input
    - strategy=truncate-characters: return first N characters
    """
    def generate(self, batch: List[Dict[str, Any]]) -> List[str]:
        strategy = self.params.get("strategy", "head-words")
        max_tokens = int(self.params.get("max_tokens", 60))
        outputs = []
        for ex in batch:
            text = ex.get("input", "")
            if strategy == "truncate-characters":
                outputs.append(text[:max_tokens])
            else:
                toks = text.split()
                outputs.append(" ".join(toks[:max_tokens]))
        return outputs
