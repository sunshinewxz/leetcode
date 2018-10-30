class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low, high = matrix[0][0], matrix[-1][-1]
        while(low < high):
            mid = (low + high) // 2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                low = mid + 1
            else:
                high = mid
        return low