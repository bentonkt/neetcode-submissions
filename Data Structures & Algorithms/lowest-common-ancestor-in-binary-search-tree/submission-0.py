# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Use DFS to find the first node that is between the two values, inclusive
        if not p:
            return q
        if not q:
            return p

        # Make sure to sort val1, val2
        def bs(root, val1, val2):
            if root == None:
                return None
            
            if val1 <= root.val and root.val <= val2:
                return root

            if root.val < val1:
                return bs(root.right, val1, val2)

            return bs(root.left, val1, val2)

        return bs(root, min(p.val, q.val), max(p.val, q.val))