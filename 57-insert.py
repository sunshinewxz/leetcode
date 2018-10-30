# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = [i.start for i in intervals]
        index = bisect.bisect_left(start, newInterval.start)
        if index > 0 and newInterval.start <= intervals[index-1].end:
            intervals[index-1].end = max(intervals[index-1].end, newInterval.end)
            index -= 1
        else:
            intervals = intervals[:index] + [newInterval] + intervals[index:]
        # if index < len(intervals)-1 and newInterval.end >= intervals[index+1].start:
        while(index < len(intervals)-1 and intervals[index].end >= intervals[index+1].start):
            intervals[index].end = max(intervals[index].end, intervals[index+1].end)
            if index + 2 < len(intervals):
                intervals = intervals[:index+1] + intervals[index+2:]
            else:
                intervals = intervals[:index+1]
        return intervals


# solution 2
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s = newInterval.start
        e = newInterval.end
        l = 0
        r = len(intervals)
        while l<r:
            mid = (l+r)/2
            if s>intervals[mid].end:
                l = mid + 1
            else:
                r = mid
        sInd = l
        l = 0
        r = len(intervals)
        while l<r:
            mid = (l+r)/2
            if e>=intervals[mid].start:
                l = mid + 1
            else:
                r = mid
        eInd = l
        if sInd!=eInd:
            intervals[sInd].start = min(intervals[sInd].start,s)
            intervals[sInd].end = max(intervals[eInd-1].end,e)
            intervals[sInd+1:eInd] = []
        else:
            intervals.insert(sInd,newInterval)
        return intervals