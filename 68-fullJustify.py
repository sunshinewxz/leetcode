class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line = []
        word_len = 0
        result = []
        for word in words:
            if word_len + len(word) + len(line) > maxWidth:
                blank = maxWidth - word_len
                temp = len(line) - 1 if len(line) > 1 else 1
                min_blank = blank // temp
                more_blank = blank - min_blank * temp
                for i in range(temp):
                    iblank = min_blank
                    if i < more_blank:
                        iblank += 1
                    line[i] += ' ' * iblank
                result.append("".join(line))
                line = []
                word_len = 0   
            line.append(word)
            word_len += len(word)
        last_blank = maxWidth - word_len - len(line) + 1
        result.append(" ".join(line) + ' '*last_blank)
        return result