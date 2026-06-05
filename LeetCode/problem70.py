class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        # Base values for 1 step and 2 steps
        one_step_back = 2
        two_steps_back = 1
        current_ways = 0
        
        # Calculate ways dynamically from step 3 up to n
        for _ in range(3, n + 1):
            current_ways = one_step_back + two_steps_back
            
            # Shift our values forward for the next loop
            two_steps_back = one_step_back
            one_step_back = current_ways
            
        return current_ways
