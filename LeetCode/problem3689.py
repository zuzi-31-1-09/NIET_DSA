class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        # Multiply the maximum possible range of the array by k
        return (max(nums) - min(nums)) * k
