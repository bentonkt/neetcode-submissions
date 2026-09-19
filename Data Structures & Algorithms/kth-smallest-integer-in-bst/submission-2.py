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

        while stack: 
            node = stack.pop()
            if not node:
                continue

            

            heapq.heappush(topk, -node.val)
            while len(topk) > k:
                heapq.heappop(topk)
            

            stack.append(node.left)
            stack.append(node.right)


        return -1 * heapq.heappop(topk)
