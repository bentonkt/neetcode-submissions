"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(oldNode): 
            if not oldNode:
                return None
            res = Node(oldNode.val)
            visited[oldNode] = res
            for n in oldNode.neighbors:
                if n in visited:
                    res.neighbors.append(visited[n])
                else:
                    res.neighbors.append(dfs(n))


            return res

        newRoot = dfs(node)

        return newRoot
