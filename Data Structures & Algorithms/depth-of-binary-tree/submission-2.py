# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        marked = set()
        queue = collections.deque()
        depth_queue = collections.deque()

        queue.append([root])
        depth_queue.append(1)

        res = 0
        while queue:
            node = queue.popleft()[0]
            depth = depth_queue.popleft()
            if node == None:
                res = max(res, depth - 1)
                continue
            

            if node.left not in marked:
                queue.append([node.left])
                depth_queue.append(depth + 1)
            if node.right not in marked:
                queue.append([node.right])
                depth_queue.append(depth + 1)

            if node.left != None:
                marked.add(node.left) 
            if node.right != None: 
                marked.add(node.right)



        return res