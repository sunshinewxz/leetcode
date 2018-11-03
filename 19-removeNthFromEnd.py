# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head
        while (n > 0):
            first = first.next
            n -= 1
            
        if first is None:
            return second.next
        while(first.next is not None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
