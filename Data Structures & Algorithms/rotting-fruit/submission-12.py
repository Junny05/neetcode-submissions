class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,-1),(0,1),(-1,0)]
        ROW, COL = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                newr, newc = q.popleft()

                for dr,dc in direction:
                    nr, nc = newr + dr, newc + dc

                    if (nr in range(ROW) and nc in range(COL) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))

            minutes += 1
        
        return minutes if fresh == 0 else -1