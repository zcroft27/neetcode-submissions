class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            diff = y - x
            if diff == 0:
                continue
            if diff > 0:
                y = diff
                heapq.heappush(stones, -y)
            if diff < 0:
                x = -diff
                heapq.heappush(stones, -x)
            
        if stones:
            return -stones[0]
        else:
            return 0