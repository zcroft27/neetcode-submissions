class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_prof = 0
        for num in prices[1:]:
            diff = num - min_so_far
            max_prof = max(max_prof, diff)
            min_so_far = min(min_so_far, num)

        return max_prof