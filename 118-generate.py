class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        index = 1
        temp = []
        result = []
        while(index <= numRows):
            if index == 1:
                temp = [1]
            elif index == 2:
                temp = [1,1]
            else:
                length = len(temp)
                temp = [temp[0]] + [temp[i] + temp[i+1] for i in range(length-1)] + [temp[-1]]
            result.append(temp)
            index += 1
        return result