class Solution:
    def reverse(self, x: int) -> int:
        numString = str(x)
        negative = False
        
        if numString[0] == "-": 
            negative = True
            numString = numString[1:]

        n = len(numString)
        reversed = ["0"] * n

        for i in range(n): 
            reversed[n-1-i] = numString[i]

        res = int("".join(reversed))

        if (not negative and res > 2 ** 31 - 1) or (negative and res > 2**31):
            return 0

        # if not negative and 1<<30 & (res) >> 1:
        #     return 0
        # if negative and (1<<30 & (res) >> 1 and not 1 & res):
        #     return 0

        if negative: 
            res *= -1

        return res

