class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        rest = self.subsets(nums[1:])
        return rest + [[nums[0]] + s for s in rest]
        # 1
        # - 2
        # - - 3
        # - - - [[]]
        # - - [[], [3]]
        # - 2 [[], [3], [2], [2,3]]
        # 1 [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]