# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow_pointer = head
        fast_pointer = head
        if slow_pointer is not None and fast_pointer.next is not None:
            while(slow_pointer is not None and fast_pointer.next is not None):
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
                if slow_pointer == fast_pointer:
                    return True
                if slow_pointer is None or fast_pointer is None:
                    return False
        return False