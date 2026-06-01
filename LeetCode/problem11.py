class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Width is the distance between the two pointers
            width = right - left
            # Height is limited by the shorter of the two vertical lines
            current_height = min(height[left], height[right])
            
            # Calculate the current water capacity
            current_water = width * current_height
            # Update the maximum water found so far
            max_water = max(max_water, current_water)
            
            # Crucial step: Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water