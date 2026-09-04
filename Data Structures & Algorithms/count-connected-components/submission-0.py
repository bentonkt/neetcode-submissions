class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # First, make adjacency list
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        # Now, run DFS on all of the connected components
        visited = set()
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for n in graph[node]:
                dfs(n)

            return True

        res = 0
        for node in range(n):
            if dfs(node):
                res+=1

        return res
        