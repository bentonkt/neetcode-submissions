"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        prev = float('-inf')

        for i in sorted(intervals, key=lambda x: x.start): 
            if i.start < prev: 
                return False
            prev = i.end
        return True