class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        
        def backtrack(i: int, total: int):
            # Base Case 1: We found a valid combination
            if total == target:
                res.append(path.copy())
                return
                
            # Base Case 2: Out of bounds or exceeded target sum
            if i >= len(candidates) or total > target:
                return
                
            # Choice 1: Include candidates[i] (allow reuse by keeping index 'i')
            path.append(candidates[i])
            backtrack(i, total + candidates[i])
            
            # Backtrack: Undo the choice to explore alternatives
            path.pop()
            
            # Choice 2: Exclude candidates[i] and move to the next number
            backtrack(i + 1, total)
            
        backtrack(0, 0)
        return res
