class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
         
        dp0 = 1
        dp1 = 1 if int(s[0]) != 0 else 0
        # result = 0
        for i in range(1, len(s)):
            result = 0
            if int(s[i]) != 0:
                result += dp1
            if 10 <= int(s[i-1:i+1]) < 27:
                result += dp0
            dp0 = dp1
            dp1 = result
        return dp1