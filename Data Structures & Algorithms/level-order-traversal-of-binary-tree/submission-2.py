# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = [root]

        while queue: 
            level = []
            nodes = queue.copy()
            queue = []
            for node in nodes: 
                if node: 
                    level.append(node.val)
                    queue.extend([node.left, node.right])

            res.append(level)

        res.pop()
            

        return res

