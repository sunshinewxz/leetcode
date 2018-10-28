class ListNode(object):
    def __init__(self, key, value):
        self.pair = [key, value]
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        if self.h[index] != None:
            cur = self.h[index]
            while(cur is not None):
                if cur.pair[0] == key:
                    return cur.pair[1]
                else:
                    cur = cur.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] != None:
            if self.h[index].pair[0] == key:
                self.h[index] = self.h[index].next
            else:
                pre = self.h[index]
                cur = self.h[index].next
                while(cur is not None):
                    if cur.pair[0] == key:
                        pre.next = cur.next
                        break
                    else:
                        cur, pre = cur.next, pre.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)