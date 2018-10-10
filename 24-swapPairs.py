# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return None
        if head.next is None:
        	return head
        result_head = head.next
        temp = ListNode(0)
        while(head.next is not None):
        	temp.next = head.next
        	tempo = head.next.next
        	head.next.next = head
        	if tempo is not None and tempo.next is not None:
        		head.next = tempo.next
        		head = tempo
        	elif tempo is None:
        		head.next = None
        	else: 
        		head.next = tempo
        		head = tempo
        return result_head

# solution 2
def swapPairs(self, head):
	if head is None or head.next is None:
		return head
	new_head = head.next
	head.next = self.swapPairs(head.next.next)
	new_head.next = head
	return new_head




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
s = Solution()
head = s.swapPairs(node1)
while (head is not None):
	print(head.val)
	head = head.next

