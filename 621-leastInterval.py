from heapq import *
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        heap = []
        for k,v in count.items():
            heappush(heap, [-1*v, k])
        result = 0
        while(len(heap) > 0):
            temp = []
            index = 0
            while(index <= n):
                result += 1
                if len(heap) > 0:
                    # print(heap)
                    v, k = heappop(heap)
                    if v != -1:
                        temp.append([v+1, k])
                if len(heap) == 0 and len(temp) == 0:
                    break
                else:
                    index += 1
            for t in temp:
                heappush(heap, t)
        return result
            
            
            