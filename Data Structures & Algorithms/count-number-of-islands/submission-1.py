class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        marked = set() # Set of coordinate tuples

        def explore(r, c):
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or grid[r][c] != '1' or (r,c) in marked:
                return
            
            marked.add((r,c))
            # Search all adjacent
            explore(r+1,c)
            explore(r-1,c)
            explore(r,c + 1)
            explore(r,c - 1)


        res = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and ((r,c) not in marked):
                    explore(r, c)
                    res += 1


        return res

