class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return self.bs(1, x, x)
        
    def bs(self, l, r, target):
        mid = (l+r) // 2
        val = mid * mid
        if val == target or r-l <= 1:
            return mid
        if val < target:
            return self.bs(mid, r, target)
        elif val > target:
            return self.bs(l, mid, target)