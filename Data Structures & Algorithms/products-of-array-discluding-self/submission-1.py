class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = 1
        suffix[n-1] = 1
        # 2,4,6,8 : 1,2,8,48 : 192,48,8,1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        output = [0]*n
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
        
        return output