class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        

        def addCell(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or (r,c) in visit or grid[r][c] == -1):
                return
            
            q.append([r,c])
            visit.add((r,c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dist += 1

