class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isValidBST(self, root):
		result = self.compare(root, None, None)
		return result


	def compare(self, root_node, min, max):
		if root_node is None:
			return True

		if (min is not None and root_node.val <= min) or (max is not None and root_node.val >= max):
			return False
		return self.compare(root_node.left, min, root_node.val) and self.compare(root_node.right, root_node.val, max)



root_node = TreeNode(10)
left_node = TreeNode(5)
right_node = TreeNode(15)
left_s = TreeNode(6)
right_s = TreeNode(20)

# root_node.val = 2
root_node.left = left_node
root_node.right = right_node
# left_node.val = 1
left_node.left = None
left_node.right = None
# right_node.val = 3
right_node.left = left_s
right_node.right = right_s
left_s.left = None
left_s.right = None
right_s.left = None
right_s.right = None
result = Solution()
print(result.isValidBST(root_node))