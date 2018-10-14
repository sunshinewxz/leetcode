class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return int(s)
        s = list(s.replace(' ',''))
        stack = []
        result = 0
        index = 0
        temp = ''
        while(index < len(s)):
            if s[index] >= '0' and s[index] <= '9':
                while(index <= len(s)-1 and s[index] >= '0' and s[index] <= '9'):
                    temp += s[index]
                    index += 1
                if index == len(s):
                    return int(temp)
                stack.append(int(temp))
                temp = ''

            if s[index] == '+':
                if s[index+1] == '(':
                    stack.append('+')
                    stack.append('(')
                    index += 2
                else:
                    index += 1
                    while(index <= len(s) - 1 and s[index] >= '0' and s[index] <= '9'):
                        temp += s[index]
                        index += 1
                    result = (int(stack.pop()) + int(temp))
                    if index == len(s):
                        return result
                    stack.append(result)
                    temp = ''


            if s[index] == '-':
                if s[index+1] == '(':
                    stack.append('-')
                    stack.append('(')
                    index += 2
                else:
                    index += 1
                    while(index <= len(s) - 1 and s[index] >= '0' and s[index] <= '9'):
                        temp += s[index]
                        index += 1
                    result = (int(stack.pop()) - int(temp))
                    if index == len(s):
                        return result
                    stack.append(result)
                    temp = ''
                    

            if s[index] == ')':
                con = int(stack.pop())
                stack.pop()
                if len(stack) > 0:
                    sig = stack.pop()
                    if sig == '+':
                        result = (int(stack.pop()) + con)
                        stack.append(result)
                    elif sig == '-':
                        result = (int(stack.pop()) - con)
                        stack.append(result)
                    else:
                        stack.append(con)
                else:
                    stack.append(con)
                index += 1
                if index == len(s):
                    return int(stack.pop())

            if s[index] == '(':
                stack.append('(')
                index += 1
        result = int(stack.pop())
        return result

# solution 2
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = num = 0
        sign = 1
        stack = []
        
        for ch in s:
            if ch.isdigit():
                num = num*10 + ord(ch)-ord("0")
            elif ch == "+":
                total += num*sign
                sign = 1
                num = 0
            elif ch == "-":
                total += num*sign
                sign = -1
                num = 0
            elif ch == "(":
                stack.append((total, sign))
                total = 0
                sign = 1
            elif ch == ")":
                total += num*sign
                num = 0
                sign = 1
                ptotal, psign = stack.pop()
                total = ptotal+psign*total
        
        if num:
            total += num*sign
        return total

s = Solution()
print(s.calculate('1-(5)'))








