class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0:
            self.area = 0
            return
        width = len(matrix[0])
        height = len(matrix)
        self.area = [[0] * (width+1) for i in range(height+1)]
        self.area[1][1] = matrix[0][0]
        for i in range(1,height+1):
            for j in range(1,width+1):
                self.area[i][j] = self.area[i-1][j] + self.area[i][j-1] - self.area[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.area[row2][col2] - self.area[row2][col1-1] - self.area[row1-1][col2] + self.area[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)