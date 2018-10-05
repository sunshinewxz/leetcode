# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        tree_dict = {}
        que = []
        que.append(root)
        tree_dict[root] = root
        while(len(que) > 0):
            node = que.pop(0)
            if node.left is not None:
                tree_dict[node.left] = node
                que.append(node.left)
            if node.right is not None:
                tree_dict[node.right] = node
                que.append(node.right)
        
        # if tree_dict.get(q.val) == tree_dict.get(p.val):
        #     return tree_dict.get(q.val)

        p_temp = tree_dict.get(p)
        p_root = []
        p_root.append(p)
        while(p_temp.val != root.val):
            p_root.append(p_temp)
            p_temp = tree_dict.get(p_temp)
        p_root.append(p_temp)

        q_temp = tree_dict.get(q)
        q_root = []
        q_root.append(q)
        while(q_temp.val != root.val):
            q_root.append(q_temp)
            q_temp = tree_dict.get(q_temp)
        q_root.append(q_temp)

        for i in p_root:
            if i in q_root:
                return i


node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4
node1.left = node0
node1.right = node8
s = Solution()
print(s.lowestCommonAncestor(node3, node5, node4).val)








