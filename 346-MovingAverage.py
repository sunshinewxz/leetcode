class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.len = size
        self.memory = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.memory) < self.len:
            self.memory.append(val)
        else:
            self.memory.pop(0)
            self.memory.append(val)
        return round(sum(self.memory)*1.0/len(self.memory),5)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)