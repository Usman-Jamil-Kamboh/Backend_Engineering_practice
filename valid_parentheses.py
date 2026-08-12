class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for ch in s :
            if ch == "(" or ch == "{" or ch == "[" :
                stack.append(ch)
            else :
                if not stack :
                    return False
                elif stack[-1] == pairs[ch]:
                    stack.pop()
                else :
                    return False 

        if not stack :
            return True 
        else:
            return False 
                
