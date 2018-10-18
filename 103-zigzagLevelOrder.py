# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        if root is None:
            return[]
        result = []
        flag = 0
        queue.append(root)
        return self.layerSet(queue, result, flag)
    
    def layerSet(self, queue, result, flag):
        if len(queue)==0:
            return result
        temp = []
        length = len(queue)
        for i in range(length):
            node = queue.pop(0)
            temp.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        if flag == 0:
            result.append(temp)
        else:
            temp.reverse()
            result.append(temp)
        return self.layerSet(queue, result, 1-flag)
            
            
        
        