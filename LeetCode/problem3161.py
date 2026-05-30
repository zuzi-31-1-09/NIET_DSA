from typing import List
import bisect

class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, i: int, val: int):
        # Update point value by tracking max
        while i <= self.size:
            self.tree[i] = max(self.tree[i], val)
            i += i & (-i)

    def query(self, i: int) -> int:
        # Retrieve range maximum from 1 to i
        max_val = 0
        while i > 0:
            max_val = max(max_val, self.tree[i])
            i -= i & (-i)
        return max_val

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Constraints max range allocation
        max_bound = min(50000, len(queries) * 3)
        
        # Collect all obstacles added throughout the timeline
        obstacles = [0, max_bound]
        for query in queries:
            if query[0] == 1:
                obstacles.append(query[1])
                
        obstacles.sort()
        
        # Build our Fenwick tree containing max gap distributions
        ft = FenwickTree(max_bound + 1)
        for i in range(1, len(obstacles)):
            ft.update(obstacles[i], obstacles[i] - obstacles[i-1])
            
        results = []
        
        # Process the queries in reverse order (backwards)
        for query in reversed(queries):
            q_type = query[0]
            x = query[1]
            
            if q_type == 1:
                # Find neighbors to merge gaps upon obstacle removal
                idx = bisect.bisect_left(obstacles, x)
                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx + 1]
                
                # Update the right neighbor's tracking distance to cover the new gap
                ft.update(next_obs, next_obs - prev_obs)
                obstacles.pop(idx)
                
            elif q_type == 2:
                sz = query[2]
                # Find the closest obstacle to the left of or at x
                idx = bisect.bisect_right(obstacles, x) - 1
                prev_obs = obstacles[idx]
                
                # Check maximum gap before previous obstacle OR remaining room up to x
                max_available_gap = max(ft.query(prev_obs), x - prev_obs)
                results.append(max_available_gap >= sz)
                
        # Reverse back to return answers in standard chronological order
        return results[::-1]
