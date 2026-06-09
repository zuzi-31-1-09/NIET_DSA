class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Start our goal post at the very last index
        goal = len(nums) - 1
        
        # Walk backward through the array from right to left
        for i in range(len(nums) - 2, -1, -1):
            # If the current position plus its max jump can reach or cross the goal
            if i + nums[i] >= goal:
                # Move the goal post forward to our current position
                goal = i
                
        # If the goal post made it all the way back to the start, return True
        return goal == 0
