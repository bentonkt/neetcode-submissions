class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0

        res=0
        substring = set()
        while r < len(s) and l<=r:
            print("l:" + str(l) + "r: " + str(r))
            while r < len(s) and s[r] not in substring:
                substring.add(s[r])
                if len(substring) > res:
                    res = len(substring)
                r+=1
            substring.remove(s[l])
            l+=1
                
        return res
