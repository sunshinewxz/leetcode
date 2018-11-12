class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        index = 0
        str.reverse()
        for i,char in enumerate(str):
            if char == ' ':
                str[index:i] = str[index:i][::-1]
                index = i+1
        str[index:] = str[index:][::-1]