# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = False
        if root is None:
            return False
        sum_ -= root.val
        if sum_ == 0 and root.left is None and root.right is None:
            return True
        if root.left is not None:
            result = result or self.hasPathSum(root.left, sum_)
        if root.right is not None:
            result = result or self.hasPathSum(root.right, sum_)
        return result

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node2.left = node3
s = Solution()
print(s.hasPathSum(node1, 6))

