class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = [0] * 26
        for char in s:
            seen[ord(char) - ord('a')] += 1
        
        for char in t:
            seen[ord(char) - ord('a')] -= 1

        for char in seen:
            if char != 0:
                return False
        
        return True