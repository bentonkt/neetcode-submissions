# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def invert(node):
            if node == None:
                return node

            temp = invert(node.right)
            node.right = invert(node.left)
            node.left = temp

            return node

            
        return invert(root)