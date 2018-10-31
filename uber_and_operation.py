# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def employeeFreeTime(self, inter1, inter2):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        interval = []
        start_, end_ = -1, 1
        for s in inter1:
            interval.append((s.start, start_))
            interval.append((s.end, end_))
        for s in inter2:
            interval.append((s.start, start_))
            interval.append((s.end, end_))
        interval = sorted(interval)
        result = []
        balance = 0
        prev = None
        for i in range(len(interval)):
            if balance <= 0 and prev is not None:
                result.append(Interval(prev, interval[i][0]))
                prev = None
            balance += interval[i][1]
            if balance < -1:
                prev = interval[i][0]
        return result

inter1 = [Interval(0,1), Interval(3,6), Interval(10,12)]
inter2 = [Interval(1,2), Interval(5,7), Interval(11, 13)]
s = Solution()
result = s.employeeFreeTime(inter1, inter2)
