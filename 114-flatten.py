# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node_list = []
        node_list = self.dfs(root, node_list)
        if len(node_list) > 1:
            for n in node_list:
                root.left = None
                root.right = n
                root = root.right
        
    def dfs(self, root, node_list):
        if root is None:
            return node_list
        node_list.append(root)
        node_list = self.dfs(root.left, node_list)
        node_list = self.dfs(root.right, node_list)
        return node_list