# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        interval_list = []
        start_, end_ = -1, 1
        for i in range(len(intervals)):
            interval_list.append((intervals[i].start, start_))
            interval_list.append((intervals[i].end, end_))
        interval_list = sorted(interval_list)
        
        balance = 0
        # prev = 0
        result = []
        for i in range(len(interval_list)):
            if balance == 0:
                prev = interval_list[i][0]
            balance += interval_list[i][1]
            if balance == 0:
                result.append(Interval(prev, interval_list[i][0]))
        return result
                