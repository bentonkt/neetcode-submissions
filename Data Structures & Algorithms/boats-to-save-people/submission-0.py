class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        def feasible(boats): 
            num = 0

            l, r = 0, len(people) - 1

            while l <= r: 
                if num >= boats: 
                    return False
                if people[r] > limit: 
                    return False

                remain = limit - people[r]
                
                if l != r and people[l] <= remain:
                    l += 1
                r -= 1
                num += 1

            return True



        l, r = 0, len(people)
        while l < r: 
            mid = l + (r-l) // 2

            if feasible(mid): 
                r = mid
            else: 
                l = mid+1

        return l