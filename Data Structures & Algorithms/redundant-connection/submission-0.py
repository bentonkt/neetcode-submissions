class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max([max(u, v) for u, v in edges])

        islands = {}
        for i in range(1, n+1):
            islands[i] = i

        rank = [1] * (n+1)

        def findParent(node):
            temp = node
            while islands[node] != node:
                node = islands[node]

            parent = node

            islands[temp] = parent
            return parent

        for u, v in edges: 
            rootX, rootY = findParent(u), findParent(v)

            if rootX == rootY:
                # cycle
                return [u, v]

            if rank[u] < rank[v]:
                # attach u to v
                islands[rootX] = rootY
                rank[rootY] += rank[rootX]

            else:
                islands[rootY] = rootX
                rank[rootX] += rank[rootY]

        return []