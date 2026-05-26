def two_sum_optimized(nums, target):
    seen_numbers = {} # This is our Hash Map (Value : Index)
    
    for current_index, current_num in enumerate(nums):
        complement = target - current_num
        
        # Check if the needed number is already in our map
        if complement in seen_numbers:
            return [seen_numbers[complement], current_index]
            
        # If not found, store the current number and its position
        seen_numbers[current_num] = current_index
        
    return []

# Test with the same numbers
numbers = [2, 7, 11, 15]
target_sum = 9

result = two_sum_optimized(numbers, target_sum)
print(f"Optimized search found indices: {result}")
