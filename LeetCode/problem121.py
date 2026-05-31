class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize your lowest buying price to a very high number
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update min_price if we find a cheaper day to buy
            if price < min_price:
                min_price = price
            # Otherwise, calculate profit if sold today and check if it's our max
            elif price- min_price > max_profit:
                max_profit = price - min_price

        return max_profit
        