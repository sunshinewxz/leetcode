import math
import re
# solution 1
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # nums = map(int, re.findall('[+-]?\d+', expression))
        nums = re.findall('[+-]?\d+', expression)
        # nums = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a, b in zip(nums[::2], nums[1::2]):
            a = int(a)
            b = int(b)
            A = A * b + a * B
            B = B * b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return str(A) + '/' + str(B)

# solution 2
from fractions import Fraction
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        result = sum(map(Fraction, expression.replace('+', ' +').replace('-', ' -').split()))
        return '{0}/{1}'.format(result.numerator, result.denominator)