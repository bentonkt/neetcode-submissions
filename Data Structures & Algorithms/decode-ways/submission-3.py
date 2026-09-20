class Solution:
    def numDecodings(self, s: str) -> int:
        
        res = 0

        dp = [0] * len(s)
        flag = False
        def dfs(i): 
            nonlocal res

            if i >= len(s): 
                return 1

            elif s[i] == "0":
                dp[i] = 0
                return 0

            elif i == len(s) - 1:
                dp[i] = 1
                return 1

            elif dp[i]: 
                return dp[i]
            
            elif s[i] == "1":
                # CHeck that its not a 10
                if i+1 < len(s) and s[i+1] == "0":
                    dp[i] = dfs(i+2)
                    return dp[i]

                # not a 0
                val1 = dfs(i+1) #1
                val2 = dfs(i+2) #1X

                dp[i] = val1 + val2
                return dp[i]
            elif s[i] == "2" and i+1 < len(s) and int(s[i+1]) <= 6: 
                if i+1 < len(s) and s[i+1] == "0":
                    dp[i] = dfs(i+2)
                    return dp[i]

                # not a 0
                val1 = dfs(i+1) #1
                val2 = dfs(i+2) #1X

                dp[i] = val1 + val2
                return dp[i]
            else:
                val = dfs(i+1)
                dp[i] = val
                return val

        dfs(0)


        return dp[0]

            