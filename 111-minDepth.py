# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [root]
        depth = 0
        while(len(stack) > 0):
            stack_len = len(stack)
            depth += 1
            for i in range(stack_len):
                node = stack.pop(0)
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        return depth