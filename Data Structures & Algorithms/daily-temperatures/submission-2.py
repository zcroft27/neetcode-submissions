class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l, r = 0, 1
        res = [0] * len(temperatures)
        while r < len(temperatures):
            while r < len(temperatures) and temperatures[l] >= temperatures[r]:
                r += 1
            if r < len(temperatures):
                res[l] = r - l
            l += 1
            r = l + 1

        return res