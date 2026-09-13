
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1,0], [0, -1], [-1, 0]]

        explored = set()
        res = 0
        islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
            
                if (row, col) in explored or grid[row][col] == 0:
                    continue
                queue = []
                queue.append((row, col))
                # print("_______")
                size = 0
                while queue: 
                    # print(queue)
                    y, x = queue.pop()

                    if (y, x) in explored:
                        continue

                    explored.add((y, x))
                    size += 1

                    if grid[y][x]:
                        for d1, d2 in directions:
                            if 0 <= y+d1 and y+d1 < len(grid) and 0 <= x+d2 and x+d2 < len(grid[0]) and grid[y+d1][x+d2] == 1:
                                if (y+d1, x+d2) not in explored:
                                    queue.append((y+d1, x+d2))

                res = max(res, size)

        return res