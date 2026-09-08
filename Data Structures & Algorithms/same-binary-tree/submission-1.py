# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True

        def dfs(n1, n2): 
            nonlocal res

            if not n1: 
                if not n2: 
                    return
                else:
                    res = False
                    return

            if not n2: 
                res = False
                return

            if n1.val != n2.val:
                res = False
                return

            dfs(n1.left, n2.left)
            dfs(n1.right, n2.right)

        dfs(p, q)

        return res