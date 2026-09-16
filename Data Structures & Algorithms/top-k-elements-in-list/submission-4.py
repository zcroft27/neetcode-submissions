class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for e in nums:
            count[e] = 1 + count.get(e, 0)
        
        bucket = [[] for _ in range(len(nums)+1)]
        for c,f in count.items():
            bucket[f].append(c)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                res += bucket[i]
            if len(res) >= k:
                break
        
        return res[:k]