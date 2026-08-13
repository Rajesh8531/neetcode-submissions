class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        leftMin = prices[0]
        for i in range(len(prices)):
            currProfit = prices[i] - leftMin
            profit = max(profit,currProfit)
            leftMin = min(leftMin,prices[i])
        return profit
        