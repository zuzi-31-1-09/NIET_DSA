class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            # If the middle element is greater than thehighest element, the minimum element must be on the right side.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is on the left side (including mid)
            else:
                high = mid

        # When Low == high, they point directly to the minimum element
        return nums[low]