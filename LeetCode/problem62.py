class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1: Initialize an empty 1D array representing the bottom row
        # We can optimize space by only keeping track of the row below us!
        row = [1] * n
        
        # Step 2: Loop through all rows from the bottom up (except the last row)
        for i in range(m - 1):
            new_row = [1] * n
            # Loop through columns from right to left (except the rightmost column)
            for j in range(n - 2, -1, -1):
                # Current cell value = Right neighbor + Down neighbor
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
            
        return row[0]
