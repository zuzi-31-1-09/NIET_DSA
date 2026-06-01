class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            # Expand the window by adding the current number
            current_sum += nums[right]

            # Shrink the window from the left as long as the condition is met
            while current_sum >= target:
                # Update the minimal Length found so far
                min_length = min(min_length, right - left + 1)

                # Remove the leftmost element and move the left pointer
                current_sum -= nums[left]
                left += 1

        # If min_length was never updated, it means no valid subarray exists
        return 0 if min_length == float('inf') else min_length