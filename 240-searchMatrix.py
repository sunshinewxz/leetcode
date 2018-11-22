class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        index = len(matrix[0])-1
        for row in matrix:
            if row[0] > target:
                return False
            while(row[index] > target):
                index -= 1
            if row[index] == target:
                return True
        return False
        