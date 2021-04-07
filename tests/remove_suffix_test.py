"""test suffix removal"""
from dnfo import remove_suffix


def test_remove_suffix():
    """testing suffix removal"""
    assert remove_suffix("j2k31h4kjhf-5", "-5") == "j2k31h4kjhf"
    assert remove_suffix("dumptruck", "truck") == "dump"
    assert remove_suffix("tapeworm", "worm") == "tape"
