class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #Left = buy, Right = sell
        maxprofit = 0    
        while len(prices) > r:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxprofit = max(maxprofit,profit)
            else:
                l = r
            r += 1
        return maxprofit
            