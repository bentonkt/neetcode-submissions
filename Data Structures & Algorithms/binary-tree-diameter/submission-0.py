# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node): 
            if not node: 
                return (0, 0) # height, best

            hL, bestL = dfs(node.left)
            hR, bestR = dfs(node.right)

            height = max(hL, hR) + 1
            best = max(bestL, bestR, hL+hR)

            return (height, best)


        h, b = dfs(root)

        return b