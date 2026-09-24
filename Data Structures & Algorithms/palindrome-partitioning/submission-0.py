class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        path = []
        res = []

        def isPalindrome(substring): 
            l, r = 0, len(substring) - 1
            while l < r:
                if substring[l] != substring[r]:
                    return False

                l+=1
                r -= 1

            return True

        def dfs(index):
            if index == len(s):
                res.append(list(path))


            for j in range(index+1, len(s)+1): 
                substring = s[index:j]
                if isPalindrome(substring):
                    path.append(substring)
                    dfs(j)
                    path.pop()

        dfs(0)
        return res
                


                    


