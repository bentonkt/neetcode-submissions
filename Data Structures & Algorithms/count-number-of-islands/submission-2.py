from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1,0], [0, -1], [-1, 0]]

        explored = set()
        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
            
                if (row, col) in explored or grid[row][col] == "0":
                    continue
                queue = deque()
                queue.append((row, col))
                # print("_______")
                while queue: 
                    # print(queue)
                    y, x = queue.popleft()

                    if (y, x) in explored:
                        continue

                    explored.add((y, x))

                    if grid[y][x]:
                        for d1, d2 in directions:
                            if 0 <= y+d1 and y+d1 < len(grid) and 0 <= x+d2 and x+d2 < len(grid[0]) and grid[y+d1][x+d2] == "1":
                                if (y+d1, x+d2) not in explored:
                                    queue.append((y+d1, x+d2))

                res+=1


        return res
                    
