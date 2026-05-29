def partition_palindrome(s: str) -> list[list[str]]:
    res = []
    part = []
    
    def is_pal(string, l, r):
        while l < r:
            if string[l] != string[r]: return False
            l += 1; r -= 1
        return True
        
    def backtrack(start):
        if start >= len(s):
            res.append(part.copy())
            return
        for end in range(start, len(s)):
            if is_pal(s, start, end):
                part.append(s[start:end + 1])
                backtrack(end + 1)
                part.pop()

    backtrack(0)
    return res
