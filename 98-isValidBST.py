# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = []
        pre_node = None
        while(root is not None or len(stack)>0):
            while(root is not None):
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right is not None and root.val >= root.right.val:
                return False
            if pre_node is not None and pre_node.val >= root.val:
                return False
            pre_node = root
            root = root.right
        return True
        