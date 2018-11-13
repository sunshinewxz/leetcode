# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.memo = {0:1}
        self.result = 0
        self.dfs(root, 0, sum)
        return self.result
        
        
    def dfs(self, root, currentsum, sum_):
        if root is None:
            return
        currentsum += root.val
        presum = currentsum - sum_
        self.result += self.memo.get(presum, 0)
        self.memo[currentsum] = self.memo.get(currentsum, 0) + 1
        self.dfs(root.left, currentsum, sum_)
        self.dfs(root.right, currentsum, sum_)
        self.memo[currentsum] -= 1