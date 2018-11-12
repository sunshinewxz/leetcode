# solution 1: O(mn) space complexity
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix[0])
        height = len(matrix)
        visited = [[True] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    visited[i][j] = False
        
        def setZero(x, y):
            for i in range(width):
                matrix[x][i] = 0
            for i in range(height):
                matrix[i][y] = 0
                
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0 and not visited[i][j]:
                    setZero(i,j)
                    visited[i][j] = True

# solution 2: constant space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        width, height = len(matrix[0]), len(matrix)
        first_row = False
        for i in range(width):
            if matrix[0][i] == 0:
                first_row = True
        for i in range(1, height):
            for j in range(width):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, height):
            for j in range(width-1, -1, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if first_row:
            matrix[0] = [0] * width