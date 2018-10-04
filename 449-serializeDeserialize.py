# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        self.getList(root, result)
        result = ','.join(str(r) for r in result)
        return result

    def getList(self, root, result):
        if root is None:
            return
        result.append(root.val)
        self.getList(root.left, result)
        self.getList(root.right, result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 1:
            return None
        pre_list = data.split(',')
        cen_list = list(map(int, pre_list))
        cen_list = sorted(cen_list)
        cen_list = list(map(str, cen_list))
        

        root = TreeNode(pre_list[0])
        root = self.construct_tree(pre_list, cen_list, root)
        return root

    def construct_tree(self, pre_list, cen_list, root):
        if len(pre_list) == 0:
            return None
        if len(pre_list) == 1:
            return TreeNode(pre_list[0])
        index = cen_list.index(pre_list[0])
        root.left = self.construct_tree(pre_list[1:index+1], cen_list[0:index], TreeNode(pre_list[1]))
        if index+1 < len(pre_list):
            root.right = self.construct_tree(pre_list[index+1:len(pre_list)], cen_list[index+1:len(pre_list)], TreeNode(pre_list[index+1]))
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Solution 2
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def doit(node):
            if node:
                vals.append(node.val)
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        
        vals = []
        doit(root)
        return vals
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def doit():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(val)
                node.left = doit()
                node.right = doit()
                return node
            
        vals = iter(data)
        return doit()

node0 = TreeNode(24)
node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(3)
node6 = TreeNode(9)
node7 = TreeNode(7)
node8 = TreeNode(35)
# node9 = TreeNode(3)

node0.left = node1
node0.right = node8
node1.left = node2
node1.right = node3
node2.left = None
node2.right = None
node3.left = None
node3.right = node4
node4.left = node5
node4.right = node6
node6.left = node7
codec = Codec()
result = codec.serialize(node0)
# print(result)
result = codec.deserialize(result)
q = []
q.append(result)
while(len(q) > 0):
    node = q.pop(0)
    print(node.val)
    if node.left is not None:
        q.append(node.left)
    if node.right is not None:
        q.append(node.right)








