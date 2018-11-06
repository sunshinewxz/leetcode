class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = 0
        for i in range(len(data)-1, -1, -1):
            temp = '{:08b}'.format(data[i])
            if temp.startswith('0'):
                if n > 0:
                    return False
            elif temp.startswith('10'):
                n += 1
                if n == 4:
                    return False
            elif temp.startswith('1' * (n+1) + '0'):
                n = 0
            else:
                return False
        return n == 0