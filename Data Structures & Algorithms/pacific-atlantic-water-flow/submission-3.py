class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i, j, visited, prev): 
            # print(i, j)
            if (i, j) in visited:
                return

            if i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0]):
                return

            num = heights[i][j]
            if num < prev: 
                return

            visited.add((i, j))

            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        resA = set()
        resP = set()

        for i in range(len(heights)):
            j = 0
            dfs(i, j, resP, float('-inf'))
            j = len(heights[0]) - 1
            dfs(i, j, resA, float('-inf'))

        for j in range(len(heights[0])):
            i = 0
            dfs(i, j, resP, float('-inf'))
            i = len(heights) - 1
            dfs(i, j, resA, float('-inf'))

        # print(resA)
        # print(resP)

        both = resA & resP
        return [list(x) for x in both]
