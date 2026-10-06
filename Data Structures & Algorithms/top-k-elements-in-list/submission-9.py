class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        minheap = []
        for num, count in freq.items():
            heapq.heappush(minheap, (count, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        while minheap:
            res.append(minheap.pop()[1])

        return res