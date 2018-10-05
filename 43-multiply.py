class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        num1 = list(num1)
        num2 = list(num2)
        if len(num1) < len(num2):
            t = num1
            num1 = num2
            num2 = t
        index_num = 0
        index = 0
        add = 0
        for j in num2[::-1]:
            add = 0
            index_num = index
            index += 1
            for i in num1[::-1]:
                temp = int(i) * int(j)
                digit = temp % 10
                result += (digit + add) * (10**index_num)
                index_num += 1
                add = int(temp / 10)
            result += add*(10**index_num)
        # result += add*(10**index_num)
        return str(result)

s = Solution()
print(s.multiply('999','999'))
