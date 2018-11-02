# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 1
        depth = self.dfs(root, depth)
        return depth
        
    def dfs(self, root, depth):
        if root is None:
            return -1
        depth = max(depth, self.dfs(root.left, depth)+1, self.dfs(root.right, depth)+1)
        return depth