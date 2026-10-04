class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        num_islands = 0
        def bfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS
            ):
                return
            
            if (grid[r][c] == "0"):
                return
            if ((r,c) in visited):
                return
            visited.add((r,c))
            bfs(r+1,c)
            bfs(r,c+1)
            bfs(r-1,c)
            bfs(r,c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    num_islands += 1
        
        return num_islands