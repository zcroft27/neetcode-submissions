class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        for char in s:
            if (char == '(' or char == '[' or char == '{'):
                seen.append(char)
            else:
                if char == ')':
                    if (len(seen) == 0 or
                        seen.pop() != '('):
                        return False
                elif char == ']':
                    if (len(seen) == 0 or
                        seen.pop() != '['):
                        return False
                elif char == '}':
                    if (len(seen) == 0 or
                        seen.pop() != '{'):
                        return False
        
        if len(seen) != 0:
            return False

        return True

