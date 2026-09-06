class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        m, n = len(matrix), len(matrix[0])
        while l <= r: 
            rowL, colL = l // n, l %n
            rowR, colR = r // n, r %n
            
            mid = (l + r) // 2
            # print(l)
            # print(r)
            # print(mid)
            # print("___")
            rowMid, colMid = mid // n, mid % n

            L = matrix[rowL][colL]
            R = matrix[rowR][colR]
            Mid = matrix[rowMid][colMid]

            if Mid > target: 
                r = mid - 1
            elif Mid < target:
                l = mid + 1
            else: 
                return True
        

        return False