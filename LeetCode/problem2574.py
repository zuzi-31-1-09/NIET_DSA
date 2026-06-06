class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for num in nums:
            # right_sum is total minus everything to the left and current number
            right_sum = total_sum - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num
            
        return answer
