class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        Os = set()
        edges = []

        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == "O" and (i == 0 or i == m-1 or j == 0 or j == n-1):
                    edges.append((i, j))
                elif x == "O":
                    Os.add((i, j))

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        while edges:
            i, j = edges.pop()

            # explore all directions
            for y, x in directions: 
                if (y+i, x+j) in Os: 
                    Os.remove((y+i, x+j))
                    edges.append(((y+i, x+j)))

        
        # now, Os is set of unreachable Os
        for i, j in Os: 
            board[i][j] = "X"
