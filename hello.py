# Linear Search function
def linear_search(arr, target):
    # Loop through every index and item in the array
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Target found! Return its position.
            
    return -1  # Target not found in the entire list

# Let's test it with an array of numbers
my_list = [10, 23, 45, 70, 11, 15]

# Test 1: Finding an item that exists
result_1 = linear_search(my_list, 70)
print(f"Target 70 found at index position: {result_1}")

# Test 2: Finding an item that does NOT exist
result_2 = linear_search(my_list, 99)
print(f"Target 99 found at index position: {result_2}")
