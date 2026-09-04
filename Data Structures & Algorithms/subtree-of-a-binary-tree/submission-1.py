# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot == None:
            return True


        # First, use dfs to find when the subroot starts
        def dfs(root, subRoot):
            if root == None:
                return False

            if root.val == subRoot.val:
                if same(root, subRoot):
                    return True
                

            return dfs(root.left, subRoot) or dfs(root.right, subRoot)


        def same(root, subRoot):
            if (root and not subRoot) or (not root and subRoot):
                return False

            if (not root):
                return True

            if root.val != subRoot.val:
                return False

            return same(root.left, subRoot.left) and same(root.right, subRoot.right)

        return dfs(root, subRoot)
        