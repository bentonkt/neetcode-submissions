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

        # BFS
        # q = collections.deque()
        # depth = 0
        # q.append(root)
        # while q:
        #     print(q)
        #     for i in range(len(q)):
        #         elem = q.popleft()
        #         if elem.left != None:
        #             q.append(elem.left) 
        #         if elem.right != None:
        #             q.append(elem.right)

        #     depth += 1
        
        # ITERATIVE DFS
        stack = []
        stack.append((root, 0))
        max_depth = 0
        while stack:
            elem = stack.pop()
            if elem[0] == None:
                max_depth = max(max_depth, elem[1])
                continue
            stack.append((elem[0].right, elem[1]+1))
            stack.append((elem[0].left, elem[1]+1))
        

            

        return max_depth