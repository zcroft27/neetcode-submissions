class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n-1):
            for j in range(1, n):
                min_height = min(heights[i], heights[j])
                area = min_height * (j-i)
                max_area = max(max_area, area)
        
        return max_area