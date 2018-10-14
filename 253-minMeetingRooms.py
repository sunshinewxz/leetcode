# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        temp = []
        result_t = 0
        result = 0
        # intervals = sorted([i for i in intervals], key=lambda d:d.start)
        for i in intervals:
            temp.append((i.start, 1))
            temp.append((i.end, -1))
        temp = sorted([t for t in temp], key=lambda d:(d[0],d[1]))
        for t in temp:
            print(t)
        for t in temp:
            result_t += t[1]
            if result_t > result:
                result = result_t
        return result




a = Interval(13,15)
b = Interval(1,13)
# c = Interval(15,20)
# a = Interval(7, 10)
# b = Interval(2, 4)
s = Solution()
print(s.minMeetingRooms([a,b]))
