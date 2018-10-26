import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.result = -sys.maxint-1
        if root is None:
            return 0
        self.dfs(root)
        return Solution.result
    
    def dfs(self, root):
        max_sum = -sys.maxint-1
        sub_sum = -sys.maxint-1
        if root is None:
            return [0,0]
        lsum = self.dfs(root.left)[1]
        rsum = self.dfs(root.right)[1]
        max_sum = max(root.val, root.val+lsum+rsum, root.val+lsum, root.val+rsum)
        Solution.result = max(Solution.result, max_sum)
        sub_sum = max(lsum+root.val, rsum+root.val, root.val)
        return [max_sum, sub_sum]