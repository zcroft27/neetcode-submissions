class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            bucket[freq].append(num)
        
        res = []
        idx = len(nums)
        while idx >= 0 and len(res) < k:
            if bucket[idx]:
                res += bucket[idx]
            idx -= 1
        
        return res[0:k]