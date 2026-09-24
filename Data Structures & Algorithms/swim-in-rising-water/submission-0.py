class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]

        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        highest = 0
        visited = set()
        while heap: 
            height, i, j = heapq.heappop(heap)

            highest = max(highest, height)

            if i == m - 1 and j == n-1: 
                return highest

            if (i, j) in visited:
                continue

            visited.add((i, j))

            

            for y, x in directions: 
                row = i + y
                col = j + x
                if 0 <= row and row < m and 0 <= col and col < n: 
                    heapq.heappush(heap, (grid[row][col], row, col))

        

