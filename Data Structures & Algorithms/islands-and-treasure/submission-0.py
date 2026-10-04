class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if (
                    r < 0 or c < 0 or
                    r >= ROWS or c >= COLS
                ):
                    continue
                if (r,c) in visited or grid[r][c] == -1:
                    continue
                
                visited.add((r,c))
                if grid[r][c] != 0:
                    grid[r][c] = dist
                q.append((r+1,c))
                q.append((r-1,c))
                q.append((r,c+1))
                q.append((r,c-1))
            dist += 1