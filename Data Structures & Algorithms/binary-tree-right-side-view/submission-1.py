from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        res = []

        queue = deque([root])

        while queue: 
            print("Level:")
            print(list(queue))
            # Go through a level
            nextLevel = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    res.append(node.val)
                
                if node.left: 
                    nextLevel.append(node.left)
                if node.right: 
                    nextLevel.append(node.right)
            queue.extend(nextLevel)


        return res