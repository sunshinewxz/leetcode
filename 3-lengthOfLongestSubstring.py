class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        start = 0
        end = start + 1
        length = 1
        while(end < len(s)):
            if s[end] in s[start:end]:
                start = s[start:end].index(s[end]) + 1 + start
                end += 1
            else:
                if end-start+1 > length:
                    length = end - start +1
                end += 1
        return length

s = Solution()
print(s.lengthOfLongestSubstring("bbtablud"))