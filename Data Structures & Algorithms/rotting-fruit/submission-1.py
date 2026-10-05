class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        count_fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    count_fresh += 1

        visited = set()
        dist = 0
        max_min = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if (
                    r < 0 or c < 0 or
                    r >= ROWS or c >= COLS
                ):
                    continue
                if grid[r][c] == 0:
                    continue
                if (r,c) in visited:
                    continue
                if grid[r][c] == 1:
                    count_fresh -= 1

                visited.add((r,c))
                max_min = max(max_min, dist)
                q.append((r+1,c))
                q.append((r-1,c))
                q.append((r,c+1))
                q.append((r,c-1))
            dist += 1
    
        return max_min if count_fresh <= 0 else -1
            