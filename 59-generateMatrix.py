class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        i, j, di, dj = 0, 0, 0, 1
        result = [[0] * n for m in range(n)]
        for k in range(1, n*n+1):
            result[i][j] = k
            if result[(i+di)%n][(j+dj)%n] !=0:
                di, dj = dj, -di
            i += di
            j += dj
        return result