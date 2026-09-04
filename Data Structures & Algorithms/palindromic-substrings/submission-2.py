class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i, c in enumerate(s): 
            # Expand palindromes out from this char as much as possible
            front = i
            back = i

            while front < len(s) and back >= 0 and s[front] == s[back]: 
                res += 1

                front += 1
                back -= 1



        
        for i in range(len(s) - 1):
            front = i
            back = i+1

            while front >= 0 and back < len(s) and s[front] == s[back]: 
                res += 1

                front -= 1
                back += 1

        return res

