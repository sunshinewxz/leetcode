class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # curr_layer and next_layer save the node information
        if root is None:
        	return
        curr_layer = []
        next_layer = []
        temp = []
        result = []
        curr_layer.append(root)
        need_rever = False
        while(len(curr_layer) > 0):
        	for node in curr_layer:
        		if node is not None:
        			temp.append(node.val)
	        		if node.left is not None:
	        			next_layer.append(node.left)
	        		if node.right is not None:
	        			next_layer.append(node.right)
        	if need_rever:
        		temp.reverse()
        		need_rever = False
        	else:
        		need_rever = True
        	result.append(temp)
        	print(temp)
        	curr_layer = next_layer
        	next_layer = []
        	temp = []
        return result

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = None
node2.right = None
node3.left = node4
node3.right = node5
result = Solution()
print(result.zigzagLevelOrder(node1))

