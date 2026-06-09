class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        left = 0
        right = 0
        farthest = 0
        
        # We stop when the 'right' boundary reaches or passes the final index
        while right < len(nums) - 1:
            # Step 1: Scan the current window to find the absolute farthest reach
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
                
            # Step 2: Jump and shift the window boundaries forward
            left = right + 1
            right = farthest
            jumps += 1
            
        return jumps
