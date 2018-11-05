class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = num = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                num = (digits[i] + 1) % 10
                carry = (digits[i] + 1) / 10
                digits[-1] = num
                continue
            num = (digits[i] + carry) % 10
            carry = (digits[i] + carry) / 10
            digits[i] = num
        if carry == 1:
            digits.insert(0, carry)
        return digits
           