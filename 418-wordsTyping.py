# solution 1: time limit error
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        index = 0
        result = 0
        for i in range(rows):
            j = 1
            temp = 0
            dp = [0] * (cols+1)
            while(j <= cols):
                if len(sentence[index]) == j-temp:
                    dp[j] = dp[j-1] + 1
                    temp = j + 1
                    index = (index + 1) % len(sentence)
                    if j < cols:
                        dp[j+1] = dp[j]
                    j += 2
                else:
                    dp[j] = dp[j-1]
                    j += 1
                if j >= cols:
                    result += dp[-1]
        result = result / len(sentence)
        return result


# solution 2:
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        result = 0
        s = ' '.join(sentence) + ' '
        for i in range(rows):
            result += cols
            while(s[result % len(s)] != ' '):
                result -= 1
            result += 1
        return result//len(s)