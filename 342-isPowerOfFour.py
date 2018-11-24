import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        x = math.log(num,4)
        return abs(round(x) - x) < 0.0000000000001