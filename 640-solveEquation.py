class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        equation = equation.replace('-', '+-')
        left_e = equation.split('=')[0]
        right_e = equation.split('=')[1]
        left_x, left_num, right_x, right_num = 0, 0, 0, 0
        for sub in left_e.split('+'):
            if sub == '':
                continue
            if sub == 'x':
                left_x += 1
            elif sub == '-x':
                left_x -= 1
            elif 'x' in sub:
                left_x += int(sub[:-1])
            else:
                left_num += int(sub)
        for sub in right_e.split('+'):
            if sub == '':
                continue
            if sub == 'x':
                right_x += 1
            elif sub == '-x':
                right_x -= 1
            elif 'x' in sub:
                right_x += int(sub[:-1])
            else:
                right_num += int(sub)
        if left_x == right_x and left_num == right_num:
            return "Infinite solutions"
        elif left_x == right_x and left_num != right_num:
            return "No solution"
        else:
            x_num = left_x-right_x
            num = right_num - left_num
            result = num/x_num
            return 'x='+str(result)