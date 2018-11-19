class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

def deleteLeaf(root, low, high):
	if root is None:
		return
	if root.right is None and root.left is None and root.val >= low and root.val <= high:
		root = None
		return root
	root.left = deleteLeaf(root.left, low, high)
	root.right = deleteLeaf(root.right, low, high)
	return root

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
deleteLeaf(node1, 3, 5)
stack = [node1]
while(len(stack)>0):
	stack_num = len(stack)
	for i in range(stack_num):
		node = stack.pop(0)
		print(node.val)
		if node.left is not None:
			stack.append(node.left)
		if node.right is not None:
			stack.append(node.right)


