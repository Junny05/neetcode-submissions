class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = float("-inf")

        for i in range(len(prices) - sell):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1
                # 0 , 1
            else:
                buy = sell
                # 1 , 2
                # 5-1 = 4
                sell += 1
        return profit if profit != float("-inf") else 0
