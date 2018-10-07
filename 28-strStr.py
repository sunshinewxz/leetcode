class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        sea_len = len(needle)
        if sea_len == 0:
            return 0
        for i in range(len(haystack)-sea_len+1):
            print(haystack[i : i+sea_len])
            if haystack[i : i+sea_len] == needle:
                return i
        return -1

s = Solution()
print(s.strStr("aaaaa", "bba"))
