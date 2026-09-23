class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, f in freq.items():
            bucket[f].append(num)
        
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if k <= 0:
                break
            if bucket[i]:
                while bucket[i] and k >= 0:
                    res.append(bucket[i].pop())
                    k -= 1
        
        return res