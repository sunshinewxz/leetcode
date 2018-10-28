# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        node = root
        self.dfs(root)
        return node
        
    def dfs(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        temp = root.left
        root.left = self.dfs(root.right)
        root.right = self.dfs(temp)
        return root