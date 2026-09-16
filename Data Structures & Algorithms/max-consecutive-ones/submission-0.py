class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0
        for n in nums:
            if n == 1:
                curr_ones += 1
            else:
                curr_ones = 0
            max_ones = max(max_ones, curr_ones)

        return max_ones