class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1): 
            if i == 0: 
                res.append(0)
            elif i == 1:
                res.append(1)
            else: 
                power = math.floor(math.log2(i))

                res.append(1+res[i-2 ** power])

        return res