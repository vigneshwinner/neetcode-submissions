class Solution:
    def isValid(self, s: str) -> bool:
        par = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char not in par:
                stack.append(char)
            else:
                if not stack or stack.pop() != par[char]:
                    return False
        
        return not stack