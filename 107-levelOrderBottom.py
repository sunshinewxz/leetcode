# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        node = root
        result = []
        temp = self.bfs(node, result)
        temp.reverse()
        return temp
        
    def bfs(self, root, result):
        stack = [root]
        # result.append([s.val for s in stack])
        while(len(stack) > 0):
            result.append([s.val for s in stack])
            stack_num = len(stack)
            for i in range(stack_num):
                node = stack.pop(0)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
        return result