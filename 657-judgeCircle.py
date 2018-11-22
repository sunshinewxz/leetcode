# solution 1
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for s in moves:
            if s == 'U':
                y -= 1
            elif s == 'D':
                y += 1
            elif s == 'L':
                x -= 1
            elif s == 'R':
                x += 1
        return x == 0 and y == 0


# solution 2
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = d = l = r = 0
        if (moves is ""): return true
        
        return ((moves.count("D") == moves.count("U")) and
                (moves.count("L") == moves.count("R")))