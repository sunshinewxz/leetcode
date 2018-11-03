class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memory = {}
        self.sum_ = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        diff = val - self.memory.get(key, 0)
        self.memory[key] = val
        for k in range(len(key)+1):
            self.sum_[key[:k]] = self.sum_.get(key[:k], 0) + diff

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix in self.sum_:
            return self.sum_[prefix]
        return 0


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)