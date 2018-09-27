class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
        	return None
        elif len(preorder) == 1:
        	return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        index_in = inorder.index(preorder[0])
        root.left = buildTree(preorder[1:index_in+1], inorder[0:index_in])
        root.right = buildTree(preorder[index_in+1:len(preorder)], inorder[index+1:len(inorder)])
        return root

root_node = TreeNode(2)
left_node = TreeNode(1)
right_node = TreeNode(3)
# left_s = TreeNode(2)
# right_s = TreeNode(20)

# root_node.val = 2
root_node.left = None
root_node.right = left_node
# left_node.val = 1
left_node.left = None
left_node.right = right_node
# right_node.val = 3
right_node.left = None
right_node.right = None
# left_s.left = None
# left_s.right = None
# right_s.left = None
# right_s.right = None
result = Solution()
result.recoverTree(root_node)