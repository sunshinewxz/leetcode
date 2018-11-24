class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        result = [1,1]
        rowIndex -= 1
        while(rowIndex > 0):
            length = len(result)
            result = [result[0]] + [result[i] + result[i+1] for i in range(length-1)] + [result[-1]]
            rowIndex -= 1
        return result