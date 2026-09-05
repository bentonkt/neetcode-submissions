import numpy as np 
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]
        # mxn
        m, n = len(text1), len(text2)
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                c1 = text1[row]
                c2 = text2[col]

                if c1 == c2:

                    memo[row][col] = 1 + memo[row+1][col+1]
                else:
                    memo[row][col] = max(memo[row+1][col], memo[row][col+1])

        return int(memo[0][0])