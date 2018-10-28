class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        strs = sorted(strs, key=lambda d:len(d))
        prefix = strs[0]
        index = 1
        while(index < len(strs)):
            if len(prefix) == 0:
                return ''
            if prefix not in strs[index] or strs[index].index(prefix) != 0:
                prefix = prefix[:-1]
            else:
                index += 1
        return prefix