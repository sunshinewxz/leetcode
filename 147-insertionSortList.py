# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        start = ListNode(0)
        current = head
        pre = start
        next = None
        while(current is not None):
            next = current.next
            while(pre.next is not None and pre.next.val < current.val):
                pre = pre.next
            current.next = pre.next
            pre.next = current
            pre = start
            current = next
        return start.next
                
        