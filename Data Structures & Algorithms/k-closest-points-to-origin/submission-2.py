class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def calculate_dist(x1,y1,x2,y2):
            return math.sqrt(pow((x1-x2),2) + pow((y1-y2),2))
        for point in points:
            dist = -1 * calculate_dist(point[0], point[1], 0, 0)
            if len(heap) >= k:
                heapq.heappushpop(heap, (dist, point))
            else:
                heapq.heappush(heap, (dist, point))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
            
        return res        