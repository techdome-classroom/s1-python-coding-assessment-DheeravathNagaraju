class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0  # If the grid is empty, there are no islands
        
        # Get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # DFS helper function to explore the land
        def dfs(x, y):
            # Mark the current land cell as visited by turning it into water ('W')
            grid[x][y] = 'W'
            
            # Explore the four possible directions (up, down, left, right)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the new position is within bounds and is land ('L')
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'L':
                    dfs(nx, ny)
        
        island_count = 0
        
        # Traverse the entire grid
        for i in range(rows):
            for j in range(cols):
                # If we find an 'L' that is not visited, it represents a new island
                if grid[i][j] == 'L':
                    island_count += 1  # Increment the island count
                    dfs(i, j)  # Perform DFS to mark all connected land as visited
        
        return island_count
