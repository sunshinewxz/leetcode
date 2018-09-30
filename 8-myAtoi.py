class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = []
        str = str.lstrip()
        if len(str) < 1:
            return 0
        if str[0] == '+' or str[0] == '-':
            result.append(str[0])
            str = str[1:]
            if len(str)==0:
                return 0
        if not (str[0] >= '0' and str[0] <= '9'):
            return 0
        for i in range(len(str)):
            if str[i] >= '0' and str[i] <= '9':
                result.append(str[i])
            else:
                break
        result = ''.join(result)
        result = max(int(result), -2**(31))
        result = min(result, 2**(31)-1)
        return result

s = Solution()
result = s.myAtoi('   +123 123')
print(result)