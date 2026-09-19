class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chests = []
        count = set()
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    chests.append((i, j))
                elif grid[i][j] == 2147483647: 
                    count.add((i, j))


        dist = 1
        while count and chests:
            temp = []
            for i, j in chests.copy():
                # Expand from chests by one
                if (i+1, j) in count:
                    count.remove((i+1, j))
                    grid[i+1][j] = dist
                    temp.append((i+1, j))
                if (i-1, j) in count:
                    count.remove((i-1, j))
                    grid[i-1][j] = dist
                    temp.append((i-1, j))
                if (i, j+1) in count:
                    count.remove((i, j+1))
                    grid[i][j+1] = dist
                    temp.append((i, j+1))
                if (i, j-1) in count:
                    count.remove((i, j-1))
                    grid[i][j-1] = dist
                    temp.append((i, j-1))

            chests = temp
            dist += 1


        





        