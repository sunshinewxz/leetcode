# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        interval = []
        start_, end_ = -1, 1
        for sch in schedule:
            for s in sch:
                interval.append((s.start, start_))
                interval.append((s.end, end_))
        interval = sorted(interval)
        result = []
        balance = 0
        prev = None
        for i in range(len(interval)):
            if balance == 0 and prev is not None:
                result.append(Interval(prev, interval[i][0]))
            balance += interval[i][1]
            if balance == 0:
                prev = interval[i][0]
        return result