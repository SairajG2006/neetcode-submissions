class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #Find dimensions of the grid we are traversing

        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0
        q = deque()

        # traverse through grid and count amount of fresh fruits, append rotten fruits to queue

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if(nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]) or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
                
            minutes += 1
        
        return minutes if fresh == 0 else -1

                
        
     