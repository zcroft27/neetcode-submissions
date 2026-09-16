class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [[], [], []]
        for num in nums:
            buckets[num].append(num)
        
        curr = 0
        for bucket in buckets:
            while bucket:
                nums[curr] = bucket.pop()
                curr += 1