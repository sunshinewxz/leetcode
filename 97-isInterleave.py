class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # solution 1: time limited
        # result = False
        # if not s1 and not s2 and not s3:
        #     return True
        # if len(s1) < len(s2):
        #     temp = s1
        #     s1 = s2
        #     s2 = temp
        # if not s2:
        #     if s1==s3:
        #         return True
        #     else:
        #         return False
        # if s3[0] != s1[0] and s3[0] != s2[0]:
        #     return False
        # if s3[0] == s1[0]:
        #     result = result or self.isInterleave(s1[1:len(s1)], s2, s3[1:len(s3)])
        # if s3[0] == s2[0]:
        #     result = result or self.isInterleave(s1, s2[1:len(s2)], s3[1:len(s3)])
        # return result
        if not s1 and not s2 and not s3:
            return True
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        print(dp)
        return dp[len(s1)][len(s2)]



s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(s.isInterleave(s1, s2, s3))

