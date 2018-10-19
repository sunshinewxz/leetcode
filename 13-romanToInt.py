class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman_dict = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        i = 0
        while(i < len(s)):
            if (s[i] == 'I' and i+1<len(s) and (s[i+1] == 'V' or s[i+1] == 'X')) or (s[i] == 'X' and i+1<len(s) and (s[i+1] == 'L' or s[i+1] == 'C')) or (s[i] == 'C' and i+1<len(s) and (s[i+1] == 'D' or s[i+1] == 'M')):
                result += roman_dict[s[i:i+2]]
                i += 2
            else:
                result += roman_dict[s[i]]
                i += 1
        return result