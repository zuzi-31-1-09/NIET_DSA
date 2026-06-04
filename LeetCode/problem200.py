class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r: int, c: int):
            # Base Case: Stop if out of bounds or if the cell is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # Sink the land by turning it into water so we don't visit it again
            grid[r][c] = "0"

            # Recursively explore all 4 adjacent directions
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left
        # Traverse the entire 2D matrix
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r,c) # Sink the entire connected island

        return island_count