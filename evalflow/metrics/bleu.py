from collections import Counter
from typing import List, Dict
import math

def _ngram_counts(tokens, n):
    return Counter(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))

def _precision(pred_tokens, ref_tokens, n):
    p_counts = _ngram_counts(pred_tokens, n)
    r_counts = _ngram_counts(ref_tokens, n)
    if not p_counts: return 0.0
    overlap=sum(min(c, r_counts.get(ng,0)) for ng,c in p_counts.items())
    total=sum(p_counts.values())
    return overlap/total if total else 0.0

def corpus_bleu(preds: List[str], refs: List[str], max_n:int=4, smooth:bool=True) -> Dict[str,float]:
    weights=[1/max_n]*max_n
    precisions=[0.0]*max_n
    hyp_len=0; ref_len=0; eps=1e-9
    for pred, ref in zip(preds, refs):
        pt=pred.split(); rt=ref.split()
        hyp_len+=len(pt); ref_len+=len(rt)
        for n in range(1,max_n+1):
            precisions[n-1]+=_precision(pt, rt, n)
    precisions=[p/max(1,len(preds)) for p in precisions]
    if smooth: precisions=[max(p,eps) for p in precisions]
    log_p=sum(w*math.log(p if p>0 else eps) for w,p in zip(weights,precisions))
    bp=1.0 if hyp_len>ref_len else math.exp(1 - ref_len/max(hyp_len,1))
    bleu=bp*math.exp(log_p)
    return {"bleu": float(bleu)}
