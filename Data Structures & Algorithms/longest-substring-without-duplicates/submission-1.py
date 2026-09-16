class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force:
        # for each character, see how far we can go
        # O(n^2)
        # Better:
        # move r if it's not in seen, else remove s[l] from seen
        # and increment l and increment r.
        # keep running score of max(width)
        l = 0
        max_length = 0
        current_window = set()
        for r in range(len(s)):
            if s[r] in current_window:
                while s[r] in current_window and l <= r:
                    current_window.remove(s[l])
                    l += 1
            current_window.add(s[r])
            max_length = max(max_length, r-l+1)
        
        return max_length