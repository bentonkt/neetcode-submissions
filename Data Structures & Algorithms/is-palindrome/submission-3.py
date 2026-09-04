class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char != " " and char.isalnum())
        start = 0
        end = len(s) - 1
        
        if len(s) == 0:
            return True        


        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        
        if s[start] != s[end]:
            return False
        return True