class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
               Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        lv3 = "Hundred"
        lv4 = "Thousand Million Billion".split()
        digit_index = 0
        result = []
        while(num):
            token, num = num % 1000, int(num / 1000)
            word = ''
            if token > 99:
                word += lv1[int(token/100)] + ' ' + lv3 + ' '
                token = token % 100
            if token > 19:
                word += lv2[int(token/10)-2] + ' '
                token = token % 10
            if token > 0:
                word += lv1[int(token)] + ' '
            word = word.strip()
            if word:
                if digit_index > 0:
                    print(digit_index-1)
                    word += ' ' + lv4[digit_index - 1]
                else:
                    word += ' '
                result.append(word)
            digit_index += 1

        return ' '.join(result[::-1]) or 'Zero'

s = Solution()
print(s.numberToWords(1000))
# print(s.numberToWords())


