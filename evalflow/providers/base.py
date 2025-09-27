from typing import List, Dict, Any

class BaseProvider:
    def __init__(self, **kwargs):
        self.params = kwargs

    def generate(self, batch: List[Dict[str, Any]]) -> List[str]:
        raise NotImplementedError
