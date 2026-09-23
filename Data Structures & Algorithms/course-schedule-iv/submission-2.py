class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        requires = defaultdict(list)

        for u, v in prerequisites:
            requires[u].append(v)

        res = []
        for src, target in queries: 

            visited = set()

            def dfs(node, target): 
                if node == target:
                    return True

                if node in visited:
                    return False

                visited.add(node)

                neighbors = requires[node]

                for neighbor in neighbors: 
                    if dfs(neighbor, target):
                        return True

                return False

            result = dfs(src, target)
            res.append(result)

        return res


        