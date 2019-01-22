# Solution 1: bfs
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [n]
        depth = 0
        while(len(stack) > 0):
            next_stack = []
            depth += 1
            for s in stack:
                large = int(s**0.5)
                if s-large*large == 0:
                    return depth
                next_stack += [s-i*i for i in range(1, large+1)]
            stack = next_stack
        return

# Solution 2: math
import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Lagrange's four-square theorem
        while(n % 4 == 0):
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while(a*a < n):
            b = int(math.sqrt(n - a*a))
            if a*a + b*b == n:
                return 1 if a == 0 or b == 0 else 2
            a += 1
        return 3