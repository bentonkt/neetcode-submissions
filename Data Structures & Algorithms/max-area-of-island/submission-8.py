class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        for i, row in enumerate(grid): 
            for j, num in enumerate(row): 
                if num:
                    # start bfs

                    stack = [[i, j]]
                    running = 0
                    while stack:
                        y, x = stack.pop()

                        if (grid[y][x] == 0):
                            continue
                        grid[y][x] = 0
                        running += 1

                        if 0 <= y+1 and y+1 < len(grid) and grid[y +1][x]:
                            stack.append([y+1, x])
                        if 0 <= x+1 and x+1 < len(grid[0]) and grid[y][x+1]:
                            stack.append([y, x+1])
                        if 0 <= y-1 and y-1 < len(grid) and grid[y-1][x]:
                            stack.append([y-1, x])
                        if 0 <= x-1 and x-1 < len(grid[0]) and grid[y][x-1]:
                            stack.append([y, x-1])

                    res = max(running, res)
                    print("_____")


        return res

                    

                         