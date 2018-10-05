class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        dict = {'(':1, ')':-1, '{':2, '}':-2, '[':3, ']':-3}
        stack = []
        # if s[0] == '(' or s[0] == '{' or s[0] == '[':
        #     stack.append(s[0])
        # else:
        #     return False
        
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    cha = stack.pop()
                    if dict.get(cha) + dict.get(s[i]) != 0:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True

s = Solution()
print(s.isValid("(}"))
