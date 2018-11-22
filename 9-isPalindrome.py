class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

# follow up
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        px = 0
        temp = x
        while(x>0):
            px = px * 10 + (x % 10)
            x = x//10
        return px == temp