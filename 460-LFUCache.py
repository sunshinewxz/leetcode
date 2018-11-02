from collections import *
class Node(object):
    def __init__(self, value):
        self.value = value
        self.freq = 1

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_node = {}
        self.freq_nodelist = defaultdict(OrderedDict)
        self.capacity = capacity
        self.min_freq = 1
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_node:
            return -1
        self.increaseFreq(key)
        return self.key_node[key].value
        
    def increaseFreq(self, key):
        curr = self.key_node[key]
        del self.freq_nodelist[curr.freq][key]
        if self.min_freq == curr.freq and len(self.freq_nodelist[self.min_freq]) == 0:
            self.min_freq += 1
        curr.freq += 1
        self.freq_nodelist[curr.freq][key] = curr
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return 
        if key in self.key_node:
            self.increaseFreq(key)
            self.key_node[key].value = value
        else:
            if self.size == self.capacity:
                del_node = self.freq_nodelist[self.min_freq].popitem(last=False)
                del self.key_node[del_node[0]]
                self.size -= 1
            
            new_node = Node(value)
            self.key_node[key] = new_node
            self.freq_nodelist[1][key] = new_node
            self.min_freq = 1
            self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)