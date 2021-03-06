# Definition for a binary tree node.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None or root.left is None:
            return
        # if root.left is None:
        #     return 
        root.left.next = root.right
        if root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
