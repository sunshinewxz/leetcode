class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_p = 0
        p_p = 0
        last_p = -1
        last_s = -1
        while(s_p < len(s)):
            if p_p < len(p) and (s[s_p] == p[p_p] or p[p_p] == '?'):
                s_p += 1
                p_p += 1
            elif p_p < len(p) and p[p_p] == '*':
                last_s = s_p
                last_p = p_p
                p_p += 1
            elif p_p > 0 and p[p_p-1] == '*':
                s_p += 1
            elif last_p > -1:
                p_p = last_p
                s_p = last_s + 1
            else:
                return False
        while(s_p < len(s)):
            return False
        while(p_p < len(p)):
            if p[p_p] == '*':
                p_p += 1
            else:
                return False
        return True
            