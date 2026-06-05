class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in ('({['):
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif (stack[-1],ch) not in [("(", ")"), ("[", "]"), ("{", "}")]:
                    return False
                stack.pop()
        return not stack   

        