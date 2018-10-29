from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        corner = sorted([(L, -H, R) for L,R,H in buildings] + [(R,0,None) for _,R,_ in buildings])
        result = [[0,0]]
        heap = [(0,float('inf'))]
        for l,negh,r in corner:
            while(l >= heap[0][1]):
                heappop(heap)
            if negh != 0:
                heappush(heap, (negh, r))
            if result[-1][1] + heap[0][0] != 0:
                result.append([l,-heap[0][0]])
        return result[1:]