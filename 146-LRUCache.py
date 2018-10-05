import collections

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        value = self.dict.get(key)
        # self.dict.pop(key)
        # self.dict[key] = value
        self.dict.move_to_end(key)
        print(value)
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        elif self.capacity == len(self.dict):
            self.dict.popitem(last=False)
        self.dict[key] = value


obj = LRUCache(2)

obj.put(1, 1)
obj.put(2, 2)
obj.get(1)       #// returns 1
obj.put(3, 3)    #// evicts key 2
obj.get(2)       #// returns -1 (not found)
obj.put(4, 4)    #// evicts key 1
obj.get(1)       #// returns -1 (not found)
obj.get(3)       #// returns 3
obj.get(4)       #// returns 4