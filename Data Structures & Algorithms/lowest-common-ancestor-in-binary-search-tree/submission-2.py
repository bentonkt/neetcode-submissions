# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = p if p.val < q.val else q
        right = p if p.val > q.val else q

        if left.val <= root.val and right.val >= root.val: 
            return root
        elif left.val <= root.val and right.val <= root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        elif left.val >= root.val and right.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)


        