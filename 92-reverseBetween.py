# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        save_node = pre
        pre.next = head
        for i in range(m-1):
            pre = pre.next
        reverse = None
        cur = pre.next
        # pre is m - 1
        for i in range(n-m+1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        pre.next.next = cur
        pre.next = reverse
        return save_node.next