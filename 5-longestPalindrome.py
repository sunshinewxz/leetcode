class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        dp = [[0]*len(s) for i in range(len(s))]
        start = 0
        end = 0
        
        for j in range(len(s)):
            for i in range(j):
                if (s[i] == s[j]) and ((j-i<=1) or (dp[i+1][j-1] == 1)):
                    dp[i][j] = 1
                    if j - i > end - start:
                        end = j
                        start = i
            dp[j][j] = 1
        return s[start:end+1]

s = Solution()
print(s.longestPalindrome("abcda"))





