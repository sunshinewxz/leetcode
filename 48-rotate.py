class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in range(n):
            for y in range(x+1, n):
                temp = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp
        for i in range(n):
            matrix[i] = matrix[i].reverse()
        return matrix




s = Solution()
data = [197,130,1]
print(s.validUtf8(data))

