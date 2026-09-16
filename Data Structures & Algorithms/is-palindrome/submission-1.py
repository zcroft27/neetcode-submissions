class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_alph = ""
        for char in s:
            if char.isalnum():
                no_alph += char
        left = 0
        right = len(no_alph) - 1

        while left <= right:
            if no_alph[left].lower() != no_alph[right].lower():
                return False
            left += 1
            right -= 1
        
        return True