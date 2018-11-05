class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                letter = ''
                num = ''
                while(len(stack) > 0):
                    le = stack.pop()
                    if le == '[':
                        break
                    letter = le + letter
                while(len(stack) > 0 and stack[-1].isdigit()):
                    n = stack.pop()
                    num = n + num
                stack.append(letter * int(num))
            else:
                stack.append(s[i])
        return "".join(stack)