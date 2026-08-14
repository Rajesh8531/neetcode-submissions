class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        best_buy = 0
        for price in prices:
            buy = price - min_value
            best_buy = max(buy,best_buy)
            min_value = min(min_value,price)
        return best_buy
        