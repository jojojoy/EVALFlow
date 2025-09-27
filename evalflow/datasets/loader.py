from typing import List, Dict
from ..utils.io import read_jsonl

def load_dataset_from_jsonl(path: str) -> List[Dict]:
    data = read_jsonl(path)
    # Expect keys: input, reference
    for i, ex in enumerate(data):
        if "input" not in ex or "reference" not in ex:
            raise ValueError(f"Example {i} missing 'input' or 'reference' keys")
    return data
