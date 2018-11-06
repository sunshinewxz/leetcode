class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        letter_dict = {}
        for l in s:
            letter_dict[l] = letter_dict.get(l, 0) + 1
        small_pos = 0
        for i in range(len(s)):
            if s[i] < s[small_pos]:
                small_pos = i
            letter_dict[s[i]] = letter_dict[s[i]] - 1
            if letter_dict[s[i]] == 0:
                break
        temp = s[small_pos+1:].replace(s[small_pos], '')
        return s[small_pos] + self.removeDuplicateLetters(temp)