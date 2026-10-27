class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            adj[v].append(u)

        courses = []
        res = []
        for i in range(numCourses): 
            if indegree[i] == 0:
                res.append(i)
                courses.append(i)

        while courses:
            course = courses.pop()

            neighbors = adj[course]

            for neighbor in neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    courses.append(neighbor)
                    res.append(neighbor)

        if sum(indegree) == 0:
            return res
        return []