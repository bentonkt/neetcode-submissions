# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root == None:
                return 0

            return 1 + max(dfs(root.left), dfs(root.right))

        if root == None:
            return 0

        q = collections.deque()
        depth = 0
        q.append(root)
        while q:
            print(q)
            for i in range(len(q)):
                elem = q.popleft()
                if elem.left != None:
                    q.append(elem.left) 
                if elem.right != None:
                    q.append(elem.right)

            depth += 1
        

            

        return depth