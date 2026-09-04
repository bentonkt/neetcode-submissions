# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        queue = deque([root])
        res = []
        while queue: 
            row = []
            temp = deque([])
            # Put current row into res
            while queue:
                elem = queue.popleft()
                if elem: 
                    row.append(elem.val)

                    # Add children of each elem to temp storage
                    temp.append(elem.left)
                    temp.append(elem.right)


            queue = temp
            res.append(row)

        res.pop()

        return res

