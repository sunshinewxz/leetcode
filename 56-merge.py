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
        if len(intervals) == 0:
            return intervals
        result = []
        stack = []
        interval_sort = sorted(intervals, key=lambda d:d.start)
        stack.append(interval_sort[0])
        for i in range(1, len(interval_sort)):
            temp = stack.pop()
            print(temp.start)
            if interval_sort[i].start <= temp.end:
                stack.append(Interval(temp.start, max(temp.end, interval_sort[i].end)))
            else:
                result.append(temp)
                stack.append(interval_sort[i])
        if len(stack)>0:
            result.append(stack.pop())
        return result


# solution 2
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # sort list by start value
        intervals.sort(key = lambda x: x.start)
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
                
        return merged