"""
https://www.techiedelight.com/find-maximum-profit-earned-at-most-k-stock-transactions/

Given a list containing future predictions of share prices, 
find the maximum profit earned by buying and selling shares at most k times 
with a constraint that a new transaction can only start after the previous transaction is complete, 
i.e., we can only hold at most one share at a time.

For example,

Input:
Stock Price: {2, 4, 7, 5, 4, 3, 5}
k = 2
 
Output: The maximum profit is 7 (sum of 5 and 2)
 
Buy at a price 2 and sell at a price 7
Buy at a price 3 and sell at a price 5
 
 
Input:
Stock Price: {1, 5, 2, 3, 7, 6, 4, 5}
k = 3
 
Output: The maximum profit is 10 (sum of 4, 5 and 1)
 
Buy at a price 1 and sell at a price 5
Buy at a price 2 and sell at a price 7
Buy at a price 4 and sell at a price 5
 
 
Input:
Stock Price: {10, 6, 8, 4, 2}
k = 2
 
Output: The maximum profit is 2
 
Buy at a price 6 and sell at a price 8
 
 
Input:
Stock Price: {10, 8, 6, 5, 4, 2}
k = 1
 
Output: The maximum profit is 0
"""


def solve(stock_price: list[int], k: int) -> int:
    max_profit = calc_max_profit(stock_price)

    return 0


def calc_max_profit(stock_price: list[int]) -> list[list[int]]:
    # max_profit[i][j] = max profit holding from i to j
    max_profit = [[0 for _ in range(len(stock_price))] for _ in range(len(stock_price))]

    # notice, max_profit[i][j] = max(max_profit[i][j-1], stock_price[j] - stock_price[i])
    for i in range(len(stock_price)):
        for j in range(i + 1, len(stock_price)):
            max_profit[i][j] = max(
                max_profit[i][j - 1], stock_price[j] - stock_price[i]
            )

    return max_profit
