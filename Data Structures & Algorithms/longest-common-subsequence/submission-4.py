import numpy as np 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * len(text2) for _ in range(len(text1))]
        # mxn
        m, n = len(text1), len(text2)
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                c1 = text1[row]
                c2 = text2[col]

                base = 0
                if col + 1 < n and memo[row][col+1] > base:
                    base = memo[row][col+1]
                if row + 1 < m and memo[row+1][col] > base:
                    base = memo[row+1][col]

                if c1 == c2: 
                    if row +1 < m and col + 1 < n:
                        base = 1 + memo[row+1][col+1]
                    else:
                        base = 1




                memo[row][col] = base

        return int(memo[0][0])