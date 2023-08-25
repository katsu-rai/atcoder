class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            buy_price = prices[i]

            for j in range(len(prices) - 1, i, -1):
                sell_price = prices[j]
                profit = sell_price - buy_price

                max_profit = max(max_profit, profit)

        return max_profit
