class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        str_list = s.split(' ')
        while '' in str_list:
            str_list.remove('')
        if len(str_list) == 0:
            return ""
        str_list.reverse()
        result = []
        for s in str_list:
            result.append(s)
        result = " ".join(result)
        return result

s = Solution()
print(s.reverseWords("  "))