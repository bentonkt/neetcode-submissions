# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def valid(root, l, r):
            if root == None:
                return True

            if not (l < root.val and root.val < r):
                return False

            return valid(root.left, l, root.val) and valid(root.right, root.val, r)


        return valid(root, -1001, 1001)