from heapq import *
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.collection = {}
        self.list = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.collection:
            index = len(self.list)
            heappush(self.collection[val], -index)
            self.list.append(val)
            return False
        else:
            self.collection[val] = [-len(self.list)]
            self.list.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.collection:
            return False
       
        last_value = self.list.pop()
        heappop(self.collection[last_value])
        if last_value == val:
            if len(self.collection[val]) == 0:
                del self.collection[val]
            return True
        index = -heappop(self.collection[val])
        heappush(self.collection[last_value], -index)
                
        self.list[index] = last_value
        if len(self.collection[val]) == 0:
            del self.collection[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        rand = random.randint(0, len(self.list)-1)
        return self.list[rand]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()