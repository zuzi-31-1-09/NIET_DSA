class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Step 1: Map each course to its prerequisite list
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            
        # Set to track courses along the current DFS execution path
        visit_set = set()
        
        def dfs(crs):
            # Base Case 1: Detected a cycle!
            if crs in visit_set:
                return False
            # Base Case 2: This course has already been verified and cleared
            if pre_map[crs] == []:
                return True
                
            visit_set.add(crs)
            
            # Recursively check all prerequisites for this course
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
                    
            # Backtrack: Remove the course from the active path
            visit_set.remove(crs)
            # Prune: Mark this course as fully verified by clearing its list
            pre_map[crs] = []
            return True
            
        # Run DFS for every single course to handle disconnected graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True
