class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        n = len(nums)
        for i in range(n):
            a = nums[i]
            if a > 0:
                # all remaining are positive,
                # impossible to find more triplets.
                break

            if i > 0 and a == nums[i-1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res