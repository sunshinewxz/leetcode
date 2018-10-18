# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node_list = []
        while(l1 is not None):
            node_list.append(l1)
            l1 = l1.next
        while(l2 is not None):
            node_list.append(l2)
            l2 = l2.next
        node_list = sorted(node_list, key=lambda d:d.val)
        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]
        node_list[-1].next = None
        return node_list[0]