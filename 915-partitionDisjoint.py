class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        min_temp = A[-1]
        minl = [0] * len(A)
        for i in range(len(A)-1,-1,-1):
            min_temp = min(min_temp, A[i])
            minl[i] = min_temp
        maxr = A[0]
        for i in range(len(A)-1):
            maxr = max(maxr, A[i])
            if maxr <= minl[i+1]:
                return i + 1
        