class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        return sorted_nums[(n // 2)]