# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do in order traversal, then go to the k-1th index

        def traversal(root):
            if root == None:
                return []

            # Get left subtree, then itself, than right subtree
            left = traversal(root.left)
            mid = root.val
            right = traversal(root.right)

            result=[]
            result = left
            result.append(mid)
            result.extend(right)

            return result

        vals = traversal(root)
        if not vals:
            return 0
        return vals[k-1]

