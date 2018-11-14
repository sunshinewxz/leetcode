# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1: iteratively
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = [root]
        while(len(stack) > 0):
            temp = []
            stack_num = len(stack)
            for s in stack:
                if s is None:
                    temp.append(None)
                else:
                    temp.append(s.val)
            if temp != temp[::-1]:
                return False
            for i in range(stack_num):
                node = stack.pop(0)
                if node is not None:
                    stack.append(node.left)
                    stack.append(node.right)
        return True
        

# solution 2: recursively
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        
        
        