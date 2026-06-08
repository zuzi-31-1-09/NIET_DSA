class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []

        def backtrack():
            # Base Case: If the current path matches the Length of nums, we found a permutation
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                # Skip if the number is already used in the current path
                if num in path:
                    continue
                    
                # Make a choice
                path.append(num)
                
                # Recurse down the decision tree
                backtrack()
                
                # Backtrack: Undo the choice to try other elements at this position
                path.pop()
                
        backtrack()
        return res