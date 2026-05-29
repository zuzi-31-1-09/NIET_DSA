class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            num_to_idx[num] = i
