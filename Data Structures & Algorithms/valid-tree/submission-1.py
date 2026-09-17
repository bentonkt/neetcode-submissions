class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(set)
        for x, y in edges:
            adj[x].add(y)
            adj[y].add(x)

        visited = set()

        stack = [0]
        while stack:
            node = stack.pop()
            print(node)
            if node in visited:
                return False
            visited.add(node)

            neighbors = adj[node]
            for ne in neighbors:
                adj[ne].remove(node)

                stack.append(ne)

        # print(visited)
        # print(len(visited))
        # print(n)
        return len(visited) == n
