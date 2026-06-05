from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        def count_waviness(S: str) -> int:
            n = len(S)
            
            @lru_cache(None)
            def dp(idx, prev1, prev2, is_tight, is_started):
                # Base Case: end of the number string reached
                if idx == n:
                    return (1, 0) if is_started else (0, 0)
                
                limit = int(S[idx]) if is_tight else 9
                total_cnt = 0
                total_sum = 0
                
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    
                    if not is_started:
                        if d == 0:
                            # Skip leading zeros
                            cnt, sm = dp(idx + 1, -1, -1, next_tight, False)
                        else:
                            cnt, sm = dp(idx + 1, d, -1, next_tight, True)
                        total_cnt += cnt
                        total_sum += sm
                    else:
                        cnt, sm = dp(idx + 1, d, prev1, next_tight, True)
                        
                        # A valid wave requires three digits (prev2 must exist)
                        is_wave = 0
                        if prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                                is_wave = 1
                        
                        total_cnt += cnt
                        total_sum += sm + is_wave * cnt
                        
                return total_cnt, total_sum

            # Directly grab index 1 to fetch only total_sum
            return dp(0, -1, -1, True, False)[1]

        # Extracting the raw sum allows clean subtraction
        ans2 = count_waviness(str(num2))
        ans1 = count_waviness(str(num1 - 1)) if num1 > 0 else 0
        
        return ans2 - ans1
