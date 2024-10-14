"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
?envType=problem-list-v2&envId=array
"""


def maxProfit(self, prices: list[int]) -> int:
    profit: int = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
