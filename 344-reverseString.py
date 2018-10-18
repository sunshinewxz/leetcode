class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s.reverse()
        return "".join(s)

        # solution 2:
        # return s[::-1]