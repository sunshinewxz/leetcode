# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        digit = 0
        node = ListNode(0)
        result = node
        while(l1 is not None and l2 is not None):
            digit = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry)/10
            node.next = ListNode(digit)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        if l1 is not None:
            while(l1 is not None):
                digit = (l1.val + carry)%10
                carry = (l1.val + carry)/10
                node.next = ListNode(digit)
                node = node.next
                l1 = l1.next
        elif l2 is not None:
            while(l2 is not None):
                digit = (l2.val + carry)%10
                carry = (l2.val + carry)/10
                node.next = ListNode(digit)
                node = node.next
                l2 = l2.next
        if carry > 0:
            node.next = ListNode(carry)
        return result.next

