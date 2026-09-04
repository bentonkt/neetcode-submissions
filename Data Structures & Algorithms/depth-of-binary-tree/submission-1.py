# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        marked = set()
        stack = []
        depth_stack = []

        stack.append(root)
        depth_stack.append(1)

        res = 0
        while stack:
            node = stack.pop()
            depth = depth_stack.pop()
            if node == None:
                res = max(res, depth - 1)
                continue
            

            if node.left not in marked:
                stack.append(node.left)
                depth_stack.append(depth + 1)
            if node.right not in marked:
                stack.append(node.right)
                depth_stack.append(depth + 1)

            if node.left != None:
                marked.add(node.left) 
            if node.right != None: 
                marked.add(node.right)



        return res