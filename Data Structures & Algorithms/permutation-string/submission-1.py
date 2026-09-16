class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        for l in range(len(s2) - len(s1) + 1):
            count_s2 = [0] * 26
            r = l
            while r < l + len(s1):
                count_s2[ord(s2[r]) - ord('a')] += 1
                if count_s2 == count_s1:
                    return True
                r += 1

        return False