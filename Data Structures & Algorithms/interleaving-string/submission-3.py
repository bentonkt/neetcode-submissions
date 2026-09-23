class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i, j] = whether its possible to form s3[i+j:] by interleaving s1[i:] with s2[i:]

        dp = {}

        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j): 
            if i + j == len(s3):
                return True

            if (i, j) in dp: 
                return dp[(i, j)]

            res1 = False
            if i < len(s1): 
                res1 = s1[i] == s3[i+j] and dfs(i+1, j)
            
            res2 = False
            if j < len(s2): 
                res2 = s2[j] == s3[i+j] and dfs(i, j+1)

            dp[(i, j)] = res1 or res2
            return res1 or res2
            
        return dfs(0, 0)

            