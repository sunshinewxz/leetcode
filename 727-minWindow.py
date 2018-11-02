import sys
class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        max_n = sys.maxint
        dp = [[max_n] * (len(S)+1) for i in range(len(T)+1)]
        for i in range(1, len(T)+1):
            for j in range(1, len(S)+1):
                if T[i-1] == S[j-1]:
                    if i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1] + 1
        res = min(dp[-1])
        if res == max_n:
            return ''
        index = dp[-1].index(res)
        return S[index-res:index]
        