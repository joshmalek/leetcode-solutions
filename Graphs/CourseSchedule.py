def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # A graph is a DAG if it has a topological sort
    # Do a depth first search, if node has been visited before, then it is not a DAG
    # Do DFS, starting from num courses, if you cant reach 0 or there is a cycle, impossible.
    # [class,prereq] prereq -> class -- [1,0] 0 -> 1, or [0,1] 1 -> 0
    
    prereqs = dict()
    visited = set()
    for i in range(numCourses):
        prereqs[i] = []
    for c,p in prerequisites:
        prereqs[c].append(p)
    #print(prereqs)
    
    def dfs(crs):
        if crs in visited:
            return False
        if prereqs[crs] == []:
            return True

        visited.add(crs)
        for pre in prereqs[crs]:
            if not dfs(pre): return False
        visited.remove(crs)
        prereqs[crs] = []
        return True
    
    for c in range(0,numCourses):
        if not dfs(c):
            return False
    return True
                    