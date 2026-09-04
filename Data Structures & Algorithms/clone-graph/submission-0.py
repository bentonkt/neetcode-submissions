"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}

        def dfs(node):
            if node in nodes: # We've already made this node
                return nodes[node]

            copy = Node()
            copy.val = node.val
            nodes[node] = copy

            neighbs = node.neighbors
            for n in neighbs:
                copy.neighbors.append(dfs(n))


            return copy


        return dfs(node) if node else None
            