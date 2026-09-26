class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])

        res = 0
        prevEnd = float('-inf')
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else: 
                prevEnd = min(prevEnd, end)
                res +=1

        return res