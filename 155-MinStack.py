class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.memo = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        mindata = self.getMin()
        if mindata is None or x < mindata:
            mindata = x
        self.memo.append([x, mindata])
        

    def pop(self):
        """
        :rtype: void
        """
        self.memo.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.memo[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.memo) == 0:
            return None
        return self.memo[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()