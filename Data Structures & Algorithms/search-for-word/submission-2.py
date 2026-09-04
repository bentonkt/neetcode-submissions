class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()

        def search(r, c, word):
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols or (r, c) in visited or len(word) == 0:
                return False

            if board[r][c] == word[0]:
                if len(word) == 1:
                    return True
                visited.add((r,c))

                s1 = search(r+1, c, word[1:])
                s2 = search(r-1, c, word[1:])
                s3 = search(r, c+1, word[1:])
                s4 = search(r, c-1, word[1:])
                visited.remove((r,c))
                return s1 or s2 or s3 or s4

            return False

        for row in range(num_rows):
            for col in range(num_cols):
                if search(row, col, word):
                    return True
                visited = set()

        return False
                