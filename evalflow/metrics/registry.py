from typing import Callable, Dict, List

def rouge_l(preds: List[str], refs: List[str]) -> Dict[str, float]:
    # simple char-level LCS approximation
    def lcs(a, b):
        dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
        for i, ca in enumerate(a, 1):
            for j, cb in enumerate(b, 1):
                dp[i][j] = dp[i-1][j-1] + 1 if ca == cb else max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    scores = []
    for p, r in zip(preds, refs):
        if not p and not r:
            scores.append(1.0); continue
        l = lcs(p, r)
        denom = len(p) + len(r)
        scores.append((2*l)/denom if denom else 0.0)
    return {"rougeL": sum(scores)/max(1, len(scores))}

def accuracy(preds: List[str], refs: List[str]) -> Dict[str, float]:
    correct = sum(int(p.strip() == r.strip()) for p, r in zip(preds, refs))
    return {"accuracy": correct / max(1, len(preds))}

from .bleu import corpus_bleu

REGISTRY: Dict[str, Callable[[List[str], List[str]], Dict[str, float]]] = {
    "rougeL": rouge_l,
    "accuracy": accuracy,
    "bleu": lambda preds, refs: corpus_bleu(preds, refs),
}

def compute(metrics: List[str], preds: List[str], refs: List[str]) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for m in metrics:
        if m not in REGISTRY:
            raise KeyError(f"Unknown metric: {m}")
        out.update(REGISTRY[m](preds, refs))
    return out
