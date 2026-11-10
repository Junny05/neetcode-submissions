class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
            else:
                buy = sell
                sell += 1
        return profit 
            
