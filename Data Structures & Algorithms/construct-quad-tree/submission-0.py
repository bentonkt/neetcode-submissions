"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':


        def dfs(row, col, size):
            if size == 1: 
                return Node(val=grid[row][col], isLeaf=True)
            
            mid = size // 2

            topLeft = dfs(row, col, mid)
            topRight = dfs(row, col+mid, mid)
            bottomLeft = dfs(row+mid, col, mid)
            bottomRight = dfs(row+mid, col+mid, mid)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val:
                return Node(val = topLeft.val, isLeaf=True)

            return Node(topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

        return dfs(0, 0, len(grid))