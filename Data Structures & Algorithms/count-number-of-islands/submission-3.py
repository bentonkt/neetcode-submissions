class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = 0
        for i, row in enumerate(grid): 
            for j, num in enumerate(row): 
                if num == "1":
                    # start bfs

                    stack = [[i, j]]
                    res += 1
                    while stack:
                        y, x = stack.pop()
                        print([y,x])
                        grid[y][x] = "0"

                        if 0 <= y+1 and y+1 < len(grid) and grid[y +1][x] == "1":
                            stack.append([y+1, x])
                        if 0 <= x+1 and x+1 < len(grid[0]) and grid[y][x+1] == "1":
                            stack.append([y, x+1])
                        if 0 <= y-1 and y-1 < len(grid) and grid[y-1][x] == "1":
                            stack.append([y-1, x])
                        if 0 <= x-1 and x-1 < len(grid[0]) and grid[y][x-1] == "1":
                            stack.append([y, x-1])


        return res

                    

                         