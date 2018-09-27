class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        value_list = []
        while(head is not None):
            value_list.append(head.val)
            head = head.next
        return self.buildBST(value_list)


    def buildBST(self, value_list):
        if (len(value_list) == 0):
            return None
        if (len(value_list) == 1):
            return TreeNode(value_list[0])
        index = int(len(value_list)/2)
        root = TreeNode(value_list[index])
        root.left = self.buildBST(value_list[0:index])
        root.right = self.buildBST(value_list[index+1:len(value_list)])
        return root

node1 = ListNode(-10)
node2 = ListNode(-3)
node3 = ListNode(0)
node4 = ListNode(5)
node5 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
result = Solution()
result.sortedListToBST(node1)
