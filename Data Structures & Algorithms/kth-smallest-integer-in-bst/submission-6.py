# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = [root]
        topk = []
        heapq.heapify(topk)

        count = 0
        res = None

        def dfs(node):
            nonlocal count
            nonlocal res

            if not node: 
                return
            

            val = dfs(node.left)
            if val:
                return val

            count += 1
            if count == k:
                res = node.val
                return node.val

            val = dfs(node.right)
            if val: 
                return val

            return

            
        dfs(root)

        return res
