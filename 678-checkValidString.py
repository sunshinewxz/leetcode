class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = cmax = 0
        for ss in s:
            if ss == '(':
                cmin += 1
                cmax += 1
            elif ss == ')':
                cmin = max(cmin-1, 0)
                cmax -= 1
            elif ss == '*':
                cmin = max(cmin-1, 0)
                cmax += 1
            if cmax < 0:
                return False
        return cmin == 0