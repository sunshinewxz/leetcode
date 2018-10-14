class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        num = 0
        total = 0
        stack = []
        pre_opt = '+'
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if i == len(s) - 1 or char in '+-*/':
                if pre_opt == '+':
                    stack.append(num)
                    num = 0
                elif pre_opt == '-':
                    stack.append(-num)
                    num = 0
                elif pre_opt == '*':
                    stack.append(stack.pop() * num)
                    num = 0
                elif pre_opt == '/':
                    stack.append(int(stack.pop()/num))
                    num = 0
                pre_opt = char
        return sum(stack)

s = Solution()
print(s.calculate('14-3/2'))









