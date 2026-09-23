class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        to_heapify = []
        for num, freq in freq.items():
            to_heapify.append((-freq, num))
        
        heapq.heapify(to_heapify)
        res = []
        for i in range(k):
            res.append(heapq.heappop(to_heapify)[1])
        
        return res
