class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        islands = defaultdict(set)
        
        for i in range(n):
            islands[i] = i
        
        
        res = n

        def findRoot(node): 
            if islands[node] == node:
                return node
            parent = findRoot(islands[node])
            
            islands[node] = parent
            return parent

        for x, y in edges:
            rootX, rootY = findRoot(x), findRoot(y)
            if rootX == rootY:
                continue
            
            islands[rootX] = islands[rootY]


            res -= 1

        return res