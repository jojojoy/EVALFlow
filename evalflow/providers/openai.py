# Placeholder for a real OpenAI provider.
# To enable: install openai and implement generate().
from typing import List, Dict, Any
from .base import BaseProvider

class OpenAIProvider(BaseProvider):
    def generate(self, batch: List[Dict[str, Any]]) -> List[str]:
        raise NotImplementedError("OpenAIProvider not wired in this offline demo.")
