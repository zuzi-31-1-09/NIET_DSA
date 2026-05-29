class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        close_to_open = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in close_to_open:
                # It's a closing bracket; check if stack is empty or mismatch occurs
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket; push onto the stack
                stack.append(char)
                
        # If stack is empty, all brackets matched perfectly
        return len(stack) == 0
