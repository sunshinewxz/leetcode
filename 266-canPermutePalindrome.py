import collections
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        num = collections.Counter(s)
        mid = [m for m, v in num.items() if v % 2 == 1]
        if len(mid) > 1:
            return False
        else:
            return True