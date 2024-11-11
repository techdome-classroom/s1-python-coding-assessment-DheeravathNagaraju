class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0 
        row = len(grid)
        col = len(grid[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y):
            grid[x][y] = 'W'
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 'L':
                    dfs(nx, ny)
        
        land_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'L':
                    land_count += 1 
                    dfs(i, j) 
        
        return land_count
