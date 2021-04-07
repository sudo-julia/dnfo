"""test remove_prefix"""
from dnfo import remove_prefix


def test_remove_prefix():
    """testing prefix removal"""
    assert remove_prefix("big-ass", "big-") == "ass"
    assert remove_prefix("5e-SRD-Ability-Scores", "5e-SRD-") == "Ability-Scores"
    assert remove_prefix("dsjfh2984rhjsdaf", "dsjfh2984rhjsda") == "f"
