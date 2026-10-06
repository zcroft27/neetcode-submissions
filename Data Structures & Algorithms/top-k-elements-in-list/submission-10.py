class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        buckets = [[] for i in range(len(nums)+1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        i = 0
        for count in range(len(buckets)-1, -1, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res

        return res