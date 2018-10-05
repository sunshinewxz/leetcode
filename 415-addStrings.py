class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        digit = 0
        result = []
        if len(num1) < len(num2):
            len_temp = num1
            num1 = num2
            num2 = len_temp
        for i in range(len(num2)):
            temp = int(num1[len(num1)-i-1]) + int(num2[len(num2)-i-1]) + carry
            carry = int(temp/10)
            digit = temp%10
            result.append(str(digit))
        len_de = len(num1) - len(num2)
        if len_de > 0:
            for i in range(len_de):
                temp = int(num1[len_de-i-1]) + carry
                carry = int(temp/10)
                digit = temp%10
                result.append(str(digit))
        if carry > 0:
            result.append(str(carry))
        result.reverse()
        result = "".join(result)
        return result
        

s = Solution()
print(s.addStrings('999','9'))