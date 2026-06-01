class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort() # Step 1: Sort the array

        for i in range(len(nums)):
            # If the base number is positive, it's impossible to sum to 0 with remaining elements
            if nums[i] > 0:
                break

            # Step 2: Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Step 3: Initialize Two Pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                     # Skip duplicate elements for the second position
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res