class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split(' ')
        for i in range(len(word)):
            word[i] = word[i][::-1]
        return " ".join(word)