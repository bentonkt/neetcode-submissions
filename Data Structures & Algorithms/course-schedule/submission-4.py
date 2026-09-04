class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Construct a graph, then check that you can visit all nodes with DFS
        graph = defaultdict(list)
        for p in prerequisites:
            pre = p[1]
            course = p[0]

            graph[course].append(pre)


        # There can't be any courses that point to each other, must be an acyclic graph

        visited = set()
        def dfs(course): 
            if course in visited:
                return False
            
            if graph[course] == []:
                return True
            
            visited.add(course)
            for p in graph[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

