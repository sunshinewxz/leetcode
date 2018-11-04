class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = low = 0
        dict = {}
        for i,c in enumerate(s):
            dict[c] = i
            if len(dict) > k:
                low = min(dict.values())
                del dict[s[low]]
                low += 1
            result = max(result, i-low+1)
        return result
            