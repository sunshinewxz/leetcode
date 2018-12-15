class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-','')
        s = s.upper()
        result = []
        length = 0
        for i in range(len(s)-K,-1,-K):
            result.append(s[i:i+K])
            result.append('-')
            length += K
        if len(s)>length or len(s) == 0:
            result.append(s[:len(s)-length])
        else:
            result.pop(-1)
        result.reverse()
        return "".join(result)
            