class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // len(matrix[0])
            col = (mid % len(matrix[0]))
            num = matrix[row][col]
            if num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
            else:
                return True
        
        return False