class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            "]" : "[",
            "}" : "{",
            ")" : "(",
        }

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif c in [")", "]", "}"]:
                if not stack: return False
                curr = stack.pop()
                if curr != matches[c]: return False
        
        return not stack