class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Clean the string (remove spaces, symbols and make it lowercase)
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Use the Two-Pointer technique to verify
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
            
        return True
