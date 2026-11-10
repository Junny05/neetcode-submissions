class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        profit, maxProfit = 0, float("-inf") 

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(profit, maxProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit if maxProfit > float("-inf") else 0