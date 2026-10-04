class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        rest = self.permute(nums[1:])
        for permutation in rest:
            for i in range(len(permutation)+1):
                res.append(permutation.copy())
                res[-1].insert(i, nums[0])

        return res