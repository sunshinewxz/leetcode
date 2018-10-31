# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        else:
            right_smallest = self.findsmallest(root.right)
            if right_smallest is None:
                return root.left
            right_smallest.left = root.left
            return root.right
            
    def findsmallest(self, root):
        if root is None:
            return None
        while(root.left is not None):
            root = root.left
        return root