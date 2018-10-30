# no duplicate
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'None'
        result = []
        prelist = self.pre_dfs(root, result)
        result = []
        postlist = self.mid_dfs(root, result)
        # print(prelist)
        # print(postlist)
        return "#".join(prelist + postlist)

    def pre_dfs(self, node, result):
        if node is None:
            return result
        result.append(str(node.val))
        result = self.pre_dfs(node.left, result)
        result = self.pre_dfs(node.right, result)
        return result

    def mid_dfs(self, node, result):
        if node is None:
            return result
        result = self.mid_dfs(node.left, result)
        result.append(str(node.val))
        result = self.mid_dfs(node.right, result)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return None
        mid = len(data) // 2
        prelist = data[:mid].split('#')
        postlist = data[mid+1:].split('#')
        root = self.construct(prelist, postlist)
        return root

    def construct(self, prelist, postlist):
        if len(prelist) == 0:
            return
        print(prelist)
        print(postlist)
        root = TreeNode(int(prelist[0]))
        index = postlist.index(prelist[0])
        root.left = self.construct(prelist[1:index + 1], postlist[0:index])
        root.right = self.construct(prelist[index + 1:], postlist[index + 1:])
        return root

# can have duplicate numbers
class Codec:

    def serialize(self, root):
        stack, prel, inl, ndict =[], [],[],{}
        while(len(stack) > 0 or root is not None):
            while(root is not None):
                ndict[root.val] = ndict.get(root.val, 0) + 1
                root.val = (root.val, ndict[root.val])
                prel.append(str(root.val[0]) + '+' + str(root.val[1]))
                stack.append(root)
                root = root.left
            root = stack.pop()
            inl.append(str(root.val[0]) + '+' + str(root.val[1]))
            root = root.right
        return "#".join(prel+inl)
        
    def deserialize(self, data):
        whole = data.split('#')
        print(whole)
        n = len(whole)//2
        prel = whole[:n]
        inl = whole[n:]
        # print(prel)
        # print(inl)
        root = self.construct(prel, inl)
        return root
        
    def construct(self, prel, inl):
        if len(prel) == 0:
            return
        root = TreeNode(int(prel[0].split('+')[0]))
        index = inl.index(prel[0])
        root.left = self.construct(prel[1:index + 1], inl[0:index])
        root.right = self.construct(prel[index + 1:], inl[index + 1:])
        return root
        