class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visit = set()
        q = deque()

        def bfs(r, c):

            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                directions = ([1,0], [-1, 0], [0, 1], [0, -1])

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr < rows and nc < cols and nr >= 0 and nc >= 0 and grid[nr][nc] == "1" and (nr, nc) not in visit:
                        q.append((nr, nc))
                        visit.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands

