class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        root = TreeNode(postorder[len(postorder)-1])
        index = inorder.index(postorder[len(postorder)-1])
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index+1:len(inorder)], postorder[index:len(postorder)-1])
        return root