class DSU:
    def __init__(self, sizes, arr) -> None:
      self.parent = arr  
      self.sizes = sizes

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, a, b): 
        p1, p2 = self.find(a), self.find(b)

        if p1 == p2: 
            return False

        if self.sizes[p1] < self.sizes[p2]:
            self.parent[p1] = p2
            self.sizes[p2] += self.sizes[p1]
        else:
            self.parent[p2] = p1
            self.sizes[p1] += self.sizes[p2]

        return True
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        sizes = [1] * n
        parents = [i for i in range(n)]

        dsu = DSU(sizes, parents)

        count = n

        for u, v in edges: 
            if dsu.union(u, v):
                n -= 1


        return n

            