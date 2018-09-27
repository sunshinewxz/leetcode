class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
'''
construct two list
sort the value and give the value to the nodes in the list
'''
    # def recoverTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: void Do not return anything, modify root in-place instead.
    #     """
    #     list_ori = []
    #     list_res = []
    #     self.treeToList(root, list_ori, list_res)
    #    	list_ori.sort()
    #     for i in range(len(list_res)):
    #     	list_res[i].val = list_ori[i]


    # def treeToList(self, root, list_ori, list_res):
    # 	if root is None:
    # 		return
    # 	self.treeToList(root.left, list_ori, list_res)
    # 	list_ori.append(root.val)
    # 	list_res.append(root)
    # 	self.treeToList(root.right, list_ori, list_res)

'''
add a pointer pre
compare the values and find out the two wrong elements
'''
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = None
        self.n2 = None
        self.pre = None
        self.compare(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        q = []
        q.append(root)
        while(len(q)>0):
        	node = q.pop(0)
        	if node is not None:
	        	print(node.val)
	        	q.append(node.left)
	        	q.append(node.right)

    def compare(self, root):
    	if root is None:
    		return
    	self.compare(root.left)
    	if self.pre is not None and self.pre.val > root.val:
    		self.n2 = root
    		if self.n1 is None:
    			self.n1 = self.pre
    	self.pre = root
    	self.compare(root.right)




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