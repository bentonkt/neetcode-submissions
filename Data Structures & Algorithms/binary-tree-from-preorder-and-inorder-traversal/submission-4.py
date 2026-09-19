# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        indices = {inorder[i]: i for i in range(len(inorder))}
        preIndex = 0

        def dfs(left, right):
            nonlocal preIndex

            if left > right:
                return None

            root = preorder[preIndex]
            rootIndex = indices[root]

            preIndex += 1
            leftTree = dfs(left, rootIndex - 1)
            rightTree = dfs(rootIndex + 1, right)

            return TreeNode(root, leftTree, rightTree)



        return dfs(0, len(inorder)-1)

