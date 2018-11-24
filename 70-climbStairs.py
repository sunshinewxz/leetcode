from scipy.special import comb
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
        	return 1
        # if n == 2:
        # 	return 2
        result = 1
        temp = n
        while(temp >= 2):
        	result += comb(n-1, temp-2)
        	n = n-1
        	temp = temp-2
        return result

# solution 2
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

s = Solution()
print(s.climbStairs(2))
