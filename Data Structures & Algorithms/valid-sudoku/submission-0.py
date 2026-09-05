class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        digits = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for row in range(9): 
            seen = set()
            for col in range(9): 
                num = board[row][col]
                if num not in digits: 
                    continue
                num = int(num)
                if num >= 1 and num <= 9 and num not in seen:
                    seen.add(num)
                else: 
                    return False

        for col in range(9): 
            seen = set()
            for row in range(9): 
                num = board[row][col]
                if num not in digits: 
                    continue
                num = int(num)
                if num >= 1 and num <= 9 and num not in seen:
                    seen.add(num)
                else: 
                    return False


        for rowBlock in range(3):
            for colBlock in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3): 
                        num = board[rowBlock*3 + row][colBlock*3 + col]
                        if num not in digits: 
                            continue
                        num = int(num)
                        if num >= 1 and num <= 9 and num not in seen:
                            seen.add(num)
                        else: 
                            return False

        return True