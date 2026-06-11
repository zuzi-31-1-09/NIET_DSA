from collections import defaultdict

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        if not edges:
            return 0
            
        MOD = 10**9 + 7
        
        # Step 1: Build the adjacency list representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # Step 2: Use DFS to find the maximum depth (number of edges from root 1)
        max_depth = 0
        
        stack = [(1, 0, 0)] # (current_node, parent_node, current_depth)
        while stack:
            node, parent, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
                
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, depth + 1))
                    
        # Step 3: Compute 2^(max_depth - 1) using fast modular exponentiation
        return pow(2, max_depth - 1, MOD)
