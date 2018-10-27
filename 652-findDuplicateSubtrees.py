# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.dict = {}
        self.result = []
        self.dfs(root)
        return self.result
        
    def dfs(self, root):
        if root is None:
            return '#'
        tree = self.dfs(root.left) + self.dfs(root.right) + str(root.val)
        if tree in self.dict and self.dict[tree] == 1:
            self.result.append(root)
        self.dict[tree] = self.dict.get(tree, 0) + 1
        return tree