from evalflow.metrics.registry import compute

def test_bleu_and_accuracy():
    preds = ["hello world", "cats are cute"]
    refs  = ["hello world", "dogs are cute"]
    m = compute(["bleu","accuracy"], preds, refs)
    assert "bleu" in m and "accuracy" in m
    assert 0.0 <= m["bleu"] <= 1.0
    assert 0.5 <= m["accuracy"] <= 1.0
