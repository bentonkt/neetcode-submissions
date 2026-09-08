# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        l, r = float('-inf'), float('inf')

        def dfs(node, l, r): 
            nonlocal res
            if not node: 
                return 

            if node.val <= l or node.val >= r:
                res = False

            dfs(node.left, l, node.val)
            dfs(node.right, node.val, r)

        dfs(root, l, r)

        return res