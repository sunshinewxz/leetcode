# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda v:v.start)
        for i in range(len(intervals)-1):
            end = intervals[i].end
            next_start = intervals[i+1].start
            if end > next_start:
                return False
        return True
            