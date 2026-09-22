class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)

        leaves = deque([])
        for i in range(n): 
            if len(adj[i]) == 1: 
                leaves.append(i)

        remaining = n
        while remaining > 2: 
            size = len(leaves)
            remaining -= size

            for i in range(len(leaves)): 
                leaf = leaves.popleft()
                parent = adj[leaf].pop()
                del adj[leaf]
                adj[parent].remove(leaf)
                if len(adj[parent]) == 1: 
                    leaves.append(parent)


        return list(adj.keys())