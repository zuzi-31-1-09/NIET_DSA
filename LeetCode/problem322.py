class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Step 1: Initialize DP array up to 'amount'
        # Fill it with a default value higher than any possible answer (amount + 1)
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Step 2: Compute minimum coins for every amount from 1 to total amount
        for i in range(1, amount + 1):
            for c in coins:
                # Only check if the coin denomination fits within the current target amount
                if i - c >= 0:
                    # Update with the minimum between keeping current combination 
                    # vs picking this coin (1) + structural solution for the remainder
                    dp[i] = min(dp[i], 1 + dp[i - c])
                    
        # Step 3: Return -1 if amount cannot be reached, otherwise return calculated min coins
        return dp[amount] if dp[amount] != amount + 1 else -1
