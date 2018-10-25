from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []
        self.small_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.small_heap) > 0 and num > self.small_heap[0]:
            heappush(self.small_heap, num)
        else:
            heappush(self.big_heap, -num)
        if len(self.big_heap) > len(self.small_heap) + 1:
            heappush(self.small_heap, -heappop(self.big_heap))
        if len(self.big_heap) < len(self.small_heap):
            heappush(self.big_heap, -heappop(self.small_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.big_heap) > len(self.small_heap):
            return -self.big_heap[0]*(1.0)
        else:
            return (self.small_heap[0] - self.big_heap[0])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()