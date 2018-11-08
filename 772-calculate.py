class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ','')
        s = s + '$'
        def subcal(stack, i):
            sign = '+'
            num = 0
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    num = num * 10 + int(c)
                    i += 1
                elif c == '(':
                    num, i = subcal([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(num*stack.pop())
                    elif sign == '/':
                        stack.append(int(stack.pop()/num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c
            return sum(stack)
        stack = []
        return subcal(stack, 0)
                    
                    
            