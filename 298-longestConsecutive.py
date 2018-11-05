# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(root, 1)]
        result = 0
        while(len(stack) > 0):
            node, path = stack.pop()
            if node.left is not None:
                stack.append((node.left, path+1 if node.left.val == node.val + 1 else 1))
            if node.right is not None:
                stack.append((node.right, path+1 if node.right.val == node.val + 1 else 1))
            result = max(result, path)
        return result