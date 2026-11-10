class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float("-inf")
        buy = 0

        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell]-prices[buy])
            else:
                buy = sell
        return profit if profit != float("-inf") else 0 