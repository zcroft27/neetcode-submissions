class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        res = 0
        max_so_far = 0
        for i, h in enumerate(height):
            max_left[i] = max_so_far
            max_so_far = max(max_so_far, height[i])

        max_so_far = 0
        for i in range(len(height)-1, -1, -1):
            max_right[i] = max_so_far
            max_so_far = max(max_so_far, height[i])

        for i in range(len(height)):
            h = height[i]
            res += max(0, min(max_left[i], max_right[i]) - h)
        
        return res