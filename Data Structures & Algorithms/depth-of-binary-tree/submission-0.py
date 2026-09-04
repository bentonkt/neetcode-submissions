# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        marked = set()


        def dfs(node):
            if node == None or node in marked:
                return 0
            marked.add(node)

            return 1 + max(dfs(node.left), dfs(node.right))

            
        return dfs(root)