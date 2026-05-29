class Solution:
    def minElement(self, nums: List[int]) -> int:
        # Initialize the global minimum to a very large number
        min_digit_sum = float('inf')
        
        for num in nums:
            current_sum = 0
            # Extract digits and sum them up mathematically
            while num > 0:
                current_sum += num % 10
                num //= 10
            
            # Update the global minimum if the current digit sum is smaller
            if current_sum < min_digit_sum:
                min_digit_sum = current_sum
                
        return min_digit_sum