import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        missing = len(t)
        start = 0
        final_s = 0
        final_e = 0
        for i in range(len(s)):
            if need[s[i]] > 0:
                missing -= 1
            need[s[i]] -= 1
            if missing == 0:
                end = i+1
                while (start < end and need[s[start]] < 0):
                    need[s[start]] += 1
                    start += 1
                if final_e == 0 or end - start <= final_e - final_s:
                    final_e, final_s = end, start
        return s[final_s:final_e]