# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # if head is None:
        #     return head
        copy_dict = dict()
        head_new = RandomListNode(0)
        temp_node = head
        temp_head = head_new
        # if temp_node is not None:
        while temp_node:
            node_new = RandomListNode(temp_node.label)
            copy_dict[temp_node] = node_new
            temp_head.next = node_new
            temp_node = temp_node.next
            temp_head = temp_head.next

        temp_node = head
        temp_head = head_new.next
        while temp_node:
            if temp_node.random is not None:
                temp_head.random = copy_dict[temp_node.random]
            temp_node = temp_node.next
            temp_head = temp_head.next
        return head_new.next