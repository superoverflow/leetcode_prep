import pytest
from src.max_profit import solve, calc_max_profit


@pytest.mark.parametrize(
    "stock_prices, k, result",
    [
        ([2, 4, 7, 5, 4, 3, 5], 2, 3),
        ([1, 5, 2, 3, 7, 6, 4, 5], 3, 10),
        ([10, 6, 8, 4, 2], 2, 2),
    ],
)
def test_case_base(stock_prices, k, result):
    assert result == solve(stock_prices, k)


def test_calc_max_profit():
    stock_price = [2, 4, 7, 5, 4, 3, 5]
    expected = [
        [0, 2, 5, 5, 5, 5, 5],
        [0, 0, 3, 3, 3, 3, 3],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    result = calc_max_profit(stock_price)
    assert expected == result
