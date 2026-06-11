class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize an array of size n + 1 filled with 0s
        dp = [0] * (n + 1)
        
        # Build our counts bottom-up from 1 up to n
        for i in range(1, n + 1):
            # Number of 1 bits = bits in (i / 2) + 1 (if i is odd)
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp
