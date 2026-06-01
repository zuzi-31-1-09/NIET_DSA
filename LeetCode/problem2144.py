class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # Sort costs from most expensive to cheapest
        cost.sort(reverse=True)
        total_cost = 0

        # Add up all candies, skipping every 3rd candy(index 2, 5, 8, ..)
        for i in range (len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]

        return total_cost