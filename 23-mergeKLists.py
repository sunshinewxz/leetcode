import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        temp = ListNode(-1)
        head = temp
        while heap:
            smallest_node = heapq.heappop(heap)[1]
            temp.next = smallest_node
            temp = temp.next
            if smallest_node.next is not None:
                heapq.heappush(heap, (smallest_node.next.val, smallest_node.next))
        return head.next