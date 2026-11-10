"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Checking if there is no overlapping between the meetings rooms
        # Which means that (start1,end1) and (start2,end2)
        # start1 <= end2 would mean theres an overlap
        
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True