class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        temp = [''] * numRows
        index = 0
        step = 1
        for char in s:
            temp[index] += char
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
        return "".join(temp)
            
            