# solution 1
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        lenx = 32 - len(x)
        leny = 32 - len(y)
        x = '0'*lenx + x
        y = '0'*leny + y
        temp = [abs(int(x[i])-int(y[i])) for i in range(32)]
        return sum(temp)

# solution 2
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        z = x ^ y
        b_z = bin(z)[2:]
        ret = 0
        for c in b_z:
            if c == '1':
                ret += 1
        return ret