# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node_list = []
        self.getNodeList(root, node_list)
        for i in range(len(node_list)-1):
            node_list[i].left = None
            node_list[i].right = node_list[i+1]

    def getNodeList(self, root, node_list):
        if root is None:
            return
        if root is not None:
            node_list.append(root)
            self.getNodeList(root.left, node_list)
            self.getNodeList(root.right, node_list)



node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(5)
node10 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = None
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
node6.left = node9
node6.right = node10
result = Solution()
print(result.pathSum(node1,22))
