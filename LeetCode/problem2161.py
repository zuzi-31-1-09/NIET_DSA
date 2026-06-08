class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = []
        equal = []
        greater = []
        
        # Partition elements into their respective groups
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
                
        # Combine the lists to maintain relative order
        return less + equal + greater
