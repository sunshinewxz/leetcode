class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = set([int(i) for t in time.split(':') for i in t])
        x,y = time.split(':')
        while True:
            x,y = (str(int(x)+1), '00') if y == '59' else (x, str(int(y)+1))
            x = '00' if int(x) > 23 else x
            x = '0' + x if len(x) < 2 else x
            y = '0' + y if len(y) < 2 else y
            if all([int(i) in digits for i in x+y]):
                return x+':'+y