# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[1]


    def dfs(self, root):
        amount = [0,0]
        if root is not None:
            amount_left = self.dfs(root.left)
            amount_right = self.dfs(root.right)
            amount[0] = amount_left[1] + amount_right[1]
            amount[1] = max(amount[0], amount_left[0] + amount_right[0] + root.val)
        return amount