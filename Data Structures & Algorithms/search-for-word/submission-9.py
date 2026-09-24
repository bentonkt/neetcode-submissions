class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        directions = [[1,0], [0,1], [-1, 0], [0, -1]]

        path = []
        visited = set()
        res = []

        def dfs(index, i, j):
            if index == len(word): 
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if board[i][j] != word[index]:
                return False

            if (i, j) in visited:
                return False

            visited.add((i, j))

            # What choices can I make
            
            for y, x in directions:
                row = y+i
                col = x+j

                

                if dfs(index+1, row, col):
                    return True

            visited.remove((i, j))


            return False

                

        for i in range(len(board)): 
            for j in range(len(board[0])):

                visited = set()
                if board[i][j] != word[0]:
                    continue

                if dfs(0, i, j):
                    return True


        return False

        