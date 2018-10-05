class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # if len(wordDict) == 0 and len(s) == 0:
        #     return True
        # if len(wordDict) == 0 or len(s) == 0:
        #     return False
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]

so = Solution()
s = ""
wordDict = ['a']
print(so.wordBreak(s, wordDict))
