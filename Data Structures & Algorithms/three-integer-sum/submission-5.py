class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for idx, target in enumerate(sorted_nums):
            if idx > 0 and sorted_nums[idx] == sorted_nums[idx-1]:
                continue
            left, right = idx+1, len(nums) - 1
            while left < right:
                the_sum = target + sorted_nums[left] + sorted_nums[right]
                if the_sum > 0:
                    right -= 1
                elif the_sum < 0:
                    left += 1
                else:
                    res.append([target, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1
        return res