from heapq import *
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        if len(quality) == 1:
            return wage[0]
        w_q = [[j*1.0/i, i*1.0, j*1.0] for i,j in zip(quality, wage)]
        w_q = sorted(w_q, key=lambda d:d[0])
        wq = w_q[K-1][0]
        quality_sum = 0.0
        for i in range(K):
            quality_sum += w_q[i][1]
        min_wage = wq * quality_sum
        q_heap = [-w[1] for w in w_q[0:K]]
        heapify(q_heap)
        for i in range(K, len(w_q)):
            quality_sum += heappop(q_heap)
            quality_sum += w_q[i][1]
            min_wage = min(min_wage, quality_sum*w_q[i][0])
            heappush(q_heap, -w_q[i][1])
        return round(min_wage,5)
        