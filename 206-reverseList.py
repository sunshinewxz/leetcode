# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # solution 1: iteratively
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if head is None or head.next is None:
    #         return head
    #     head_temp = head
    #     node = head.next
    #     while (node is not None):
    #         # print(node.val)
    #         temp = node.next
    #         node.next = head
    #         head = node
    #         node = temp
    #     head_temp.next = None
    #     return head

    # solution 2: recursively
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        return self.reverseConnect(head, None)


    def reverseConnect(self, curr_node, pre_node):
        if curr_node.next is None:
            curr_node.next = pre_node
            return curr_node
        node_temp = curr_node.next
        curr_node.next = pre_node
        return self.reverseConnect(node_temp, curr_node)





s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
result = s.reverseList(node1)
while(result is not None):
    print(result.val)
    result = result.next

