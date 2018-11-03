# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reve = None
        fast = slow = head
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            temp = slow.next
            temp_r = reve
            reve = slow
            reve.next = temp_r
            slow = temp
        if fast is not None:
            slow = slow.next
        while(slow is not None and slow.val == reve.val):
            slow = slow.next
            reve = reve.next
        if slow is None:
            return True
        return False
        
        