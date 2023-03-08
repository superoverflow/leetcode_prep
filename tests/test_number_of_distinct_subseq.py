import pytest

from src.number_of_distinct_subseq import solve, move

def test_solve_base_case():
    assert 7 == solve("rrlrlr", 6, 1, 2)


@pytest.mark.parametrize("sequence, result", [
    ("rl", 0),
    ("lr", 0),
    ("lllr", -2)
])
def test_move(sequence, result):
    assert result == move(sequence)