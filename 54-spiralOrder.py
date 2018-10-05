class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        self.round(matrix, 0, 0, len(matrix), len(matrix[0]), result)
        return result
        
    def round(self, matrix, x, y, len_x, len_y, result):
        if (len(result) == len(matrix) * len(matrix[0])):
            return
        if matrix[x][y] is None:
            return
        dx = x
        dy = y
        while(y < len(matrix[0]) and matrix[x][y] is not None):
            result.append(matrix[x][y])
            matrix[x][y] = None
            y += 1
        y -= 1
        x += 1
        while(x < len(matrix) and matrix[x][y] is not None):
            result.append(matrix[x][y])
            matrix[x][y] = None
            x += 1
        x -=1
        y -= 1
        while(y >= dy and matrix[x][y] is not None):
            result.append(matrix[x][y])
            matrix[x][y] = None
            y -= 1
        y += 1
        x -= 1
        while(x > dx and matrix[x][y] is not None):
            result.append(matrix[x][y])
            matrix[x][y] = None
            x -= 1
        x += 1
        y += 1
        self.round(matrix, x, y, len_x, len_y, result)

s = Solution()
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(s.spiralOrder(matrix))





