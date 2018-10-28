# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def getHeight(root):
            if root is None:
                return 0
            else:
                return 1 + max(getHeight(root.left), getHeight(root.right))
        
        def update(node, row, left, right):
            if node is None:
                return
            mid = (left + right) // 2
            result[row][mid] = str(node.val)
            update(node.left, row+1, left, mid-1)
            update(node.right, row+1, mid+1, right)
            
        height = getHeight(root)
        width = 2 ** height - 1
        print(width)
        result = [[""] * width for i in range(height)]
        print(result)
        update(root, 0, 0, width-1)
        return result
        