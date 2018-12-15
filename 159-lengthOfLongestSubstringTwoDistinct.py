class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        a,b = None, None
        result = 0
        b_num = 0
        cur = 0
        for char in s:
            if char == b:
                b_num += 1
                cur += 1
            elif char == a:
                b_num = 1
                cur += 1
                a,b = b, char
            else:
                cur = b_num + 1
                b_num = 1
                a,b = b, char
            result = max(result, cur)
        return result