# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        fast = slow = head
        while(fast is not None and fast.next is not None and slow is not None):
            fast = fast.next.next
            slow = slow.next
            if fast is not None and slow is not None and fast is slow:
                break
        if fast is None or slow is None or fast.next is None:
            return
        fast = head
        while(fast is not slow):
            fast = fast.next
            slow = slow.next
        # print(slow.val)
        return slow
  