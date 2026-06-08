class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def backtrack(i: int):
            # Base Case: If we've made a choice for every element, add a copy to results
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Choice 1: Include nums [i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Backtrack: Remove nums[i] to try the alternative route
            subset.pop()

            # Choice 2: Exclude nums[i]
            backtrack(i + 1)

        # Start the recursive backtracking from index 0
        backtrack(0)
        return res