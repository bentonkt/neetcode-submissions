class Solution:
    def longestPalindrome(self, s: str) -> str:
        greatest = 0
        res = ""
        for i in range(len(s)): 
            # this is the center
            l, r = i-1, i+1
            length = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r+=1
                length += 2

            if length > greatest:
                greatest = length
                res = s[l+1:r]

            # i, i+1 pair is the center
            if i+1 < len(s) and s[i] == s[i+1]:
                l, r = i-1, i+2
                length = 2
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r+=1
                    length += 2

                if length > greatest:
                    greatest = length
                    res = s[l+1:r]

        return res