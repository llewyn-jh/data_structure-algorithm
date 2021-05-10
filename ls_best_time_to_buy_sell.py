"""Best time to buy and sell, leetcode 121"""

import time
import sys

def max_profit(prices: list) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit

if __name__ == "__main__":

    ex = [7, 1, 5, 3, 6, 4]
    start = time.time()
    max_profit(ex)
    print(f"Runtime: {time.time() - start:0.9f}")
