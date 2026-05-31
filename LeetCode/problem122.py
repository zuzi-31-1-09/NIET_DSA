class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0


        # Loop through the array starting from the second day
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, capture the profit
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit