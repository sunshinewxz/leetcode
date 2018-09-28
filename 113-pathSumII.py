# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        all_list = []
        temp = []
        if root is not None:
            temp.append(root.val)
        self.getPathSum(root, all_list, temp, sum)
        return all_list

        

    def getPathSum(self, root, all_list, temp, sum):
        if root is None:
            return
        sum -= root.val
        if sum==0 and root.left is None and root.right is None:
            all_list.append(temp)
        if root.left is not None:
            self.getPathSum(root.left, all_list, temp + [root.left.val], sum)
        if root.right is not None:
            self.getPathSum(root.right, all_list, temp + [root.right.val], sum)
        



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
