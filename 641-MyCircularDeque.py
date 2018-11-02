class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.head = None
        self.tail = None
        self.capacity = k
        self.size = 0
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = ListNode(value)
        else:
            head_next = self.head
            insert_node = ListNode(value)
            insert_node.next = head_next
            head_next.prev = insert_node
            self.head = insert_node
        self.size += 1
        return True
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = ListNode(value)
        else:
            last = self.tail
            insert_node = ListNode(value)
            last.next = insert_node
            insert_node.prev = last
            self.tail = insert_node
        self.size += 1
        return True
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self.size == 1:
            self.head = self.tail = None
        else:
            temp = self.head.next
            temp.prev = None
            self.head = temp
        self.size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self.size == 1:
            self.head = self.tail = None
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail = temp
        self.size -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.val

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.size == 0:
            return True
        return False
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.size == self.capacity:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()