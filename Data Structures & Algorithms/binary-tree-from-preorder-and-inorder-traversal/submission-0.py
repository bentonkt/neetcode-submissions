# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        

        def helper(preorder, inorder):
            if len(preorder) == 0:
                return None
            # root is first value in preorder:
            root = TreeNode(val=preorder[0])

            index = inorder.index(root.val)

            left_pre = []
            right_pre = []
            for val in preorder[1:]:
                if val in inorder[:index]:
                    left_pre.append(val)
                else:
                    right_pre.append(val)

            root.left = helper(left_pre, inorder[:index])
            root.right = helper(right_pre, inorder[index+1:])
            return root


        return helper(preorder, inorder)