# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root, [], result, sum_)
        return result

    
    def dfs(self, root, node_temp, result, sum_):
        if root is None:
            return
        sum_ -= root.val
        if sum_ == 0 and root.left is None and root.right is None:
            result.append(node_temp + [root.val])
        if root.left is not None:
            self.dfs(root.left, node_temp + [root.val], result, sum_)
        if root.right is not None:
            self.dfs(root.right, node_temp + [root.val], result, sum_)

