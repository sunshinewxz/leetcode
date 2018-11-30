# better solution
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ''
        for n, v in zip(numerals, values):
            res += (num // v) * n
            num %= v 
        return res


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        if num >= 1000:
            result += 'M' * (num//1000)
            num = num % 1000
        if num >= 900:
            result += 'CM'
            num -= 900
        if num >= 500:
            result += 'D'
            num -= 500
        if num >= 400:
            result += 'CD'
            num -= 400
        if num >= 100:
            result += 'C' * (num//100)
            num = num % 100
        if num >= 90:
            result += 'XC'
            num -= 90
        if num >= 50:
            result += 'L'
            num -= 50
        if num >= 40:
            result += 'XL'
            num -= 40
        if num >= 10:
            result += 'X' * (num//10)
            num = num % 10
        if num >= 9:
            result += 'IX'
            num -= 9
        if num >= 5:
            result += 'V'
            num -= 5
        if num >= 4:
            result += 'IV'
            num -= 4
        if num >= 1:
            result += 'I' * num
        return result