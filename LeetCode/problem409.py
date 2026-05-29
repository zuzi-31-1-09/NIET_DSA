class Solution:
    def longestPalindrome(self, s:str) -> int:
        char_set = set()
        length = 0

        # Find matching pairs dynamically
        for char in s:
            if char in char_set:
                length += 2
                char_set.remove(char)
            else:
                char_set.add(char)

        # If there are any leftover unique elements, we can place one in the center
        if char_set:
            length +=1
        
        return length