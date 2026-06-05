from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes = 0
        
        # Step 1: Initialize queue with rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes are needed
        if fresh_oranges == 0:
            return 0
            
        # Directions array for moving Up, Down, Left, Right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Step 2: Process the queue layer by layer (BFS)
        while queue and fresh_oranges > 0:
            minutes += 1
            # Process all oranges currently rotten at this specific minute
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    neighbor_r = r + dr
                    neighbor_c = c + dc
                    
                    # If neighbor is valid and fresh, infect it
                    if (0 <= neighbor_r < rows and 
                        0 <= neighbor_c < cols and 
                        grid[neighbor_r][neighbor_c] == 1):
                        
                        grid[neighbor_r][neighbor_c] = 2
                        fresh_oranges -= 1
                        queue.append((neighbor_r, neighbor_c))
                        
        # Step 3: Verify if any fresh oranges survived the outbreak
        return minutes if fresh_oranges == 0 else -1
