class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        memo = {}
        def numHours(k): 
            if k == 0:
                return float('inf')
            res = 0
            for pile in piles:
                res += math.ceil(pile / k)

            memo[k] = res
            return res

        l, r = 1, max(piles)

        while l <= r: 
            mid = (l + r) // 2
            midHours = numHours(mid)

            if midHours > h: 
                l = mid + 1
            elif midHours <= h and numHours(mid - 1) > h: 
                return mid
            else: 
                r = mid - 1


        