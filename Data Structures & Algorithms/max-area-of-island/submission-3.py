class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c,curr):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS):
                return 0
            if grid[r][c] == 0: return 0
            if (r,c) in visited: return 0
            visited.add((r,c))    
            
            return (1 + dfs(r+1,c,curr+1) +
            dfs(r-1,c,curr+1) +
            dfs(r,c+1,curr+1) +
            dfs(r,c-1,curr+1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c,0))

        return max_area