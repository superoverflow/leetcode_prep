import pytest

from src.get_rank import solve


@pytest.mark.parametrize("numbers, result", [
    ([5, 1, 3, 2, 4], [1, 5, 3, 4, 2]),
    ([4, 1, 3, 1, 4], [1, 4, 3, 5, 2])
])
def test_solve(numbers, result):
    assert result == solve(numbers)
