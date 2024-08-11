class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for x in range(len(prices)):
            if x == (len(prices) - 1):
                return maxProfit
            elif prices[(x + 1)] > prices[x]:
                maxProfit = ((prices[(x + 1)] - prices[x]) + maxProfit)