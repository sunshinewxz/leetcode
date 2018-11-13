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

# second time
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lv1 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        lv2 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        lv3 = ['Hundred']
        lv4 = ['Thousand','Million','Billion']
        
        result = []
        digit_index = 0
        while(num > 0):
            temp, num = num % 1000, int(num / 1000)
            word = ''
            if temp > 99:
                word += lv1[int(temp/100)] + ' ' + lv3[0] + ' '
                temp = temp % 100
            if temp > 19:
                word += lv2[int(temp/10)-2] + ' '
                temp = temp % 10
            if temp > 0:
                word += lv1[int(temp)] + ' '
            word = word.strip()
            # print(word)
            if len(word) > 0:
                if digit_index > 0:
                    word += ' ' + lv4[digit_index-1]
                result.append(word)
            digit_index += 1
        return " ".join(result[::-1]) or 'Zero'
        


