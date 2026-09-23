class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        l, r = 0, len(intervals)

        while l < r:
            mid = l + (r-l) // 2

            if intervals[mid][0] > newInterval[0]:
                r = mid
            else: 
                l = mid+1

        start = l - 1
            
        if start < 0 or newInterval[1] > intervals[start][1]:
            index = l
            rPrime = newInterval[1]

            while index < len(intervals) and intervals[index][0] <= newInterval[1]:
                l2, r2 = intervals[index]
                intervals.pop(index)

                rPrime = max(r2, rPrime)
        else:
            rPrime = intervals[start][1]

        if start < 0: 
            intervals.insert(0, [newInterval[0], rPrime])
            return intervals


        l1, r1 = intervals[start]

        if r1 < newInterval[0]:
            intervals.insert(start+1, [newInterval[0], rPrime])
        else:
            intervals[start] = [l1, rPrime]

        return intervals
            
