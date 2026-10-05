class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max_area = 0
        while l < r:
            height = min(heights[l], heights[r])
            max_area = max(max_area, height*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area