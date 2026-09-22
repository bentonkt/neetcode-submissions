class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        requires = defaultdict(set)
        for u, v in prerequisites: 
            requires[v].add(u)


        visited = set()
        def dfs(course): 
            if course in visited: 
                return

            visited.add(course)
            for c in requires[course].copy():
                dfs(c)
                requires[course].update(requires[c])

        for i in range(numCourses): 
            dfs(i)


        res = []
        for u, v in queries: 
            res.append(u in requires[v])



        return res