# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        new_node = UndirectedGraphNode(node.label)
        node_dict = {}
        node_dict[node] = new_node
        stack = [node]
        while(len(stack) != 0):
            ori = stack.pop()
            for nei in ori.neighbors:
                if nei not in node_dict:
                    nei_co = UndirectedGraphNode(nei.label)
                    node_dict[nei] = nei_co
                    stack.append(nei)
                node_dict[ori].neighbors.append(node_dict[nei])
        return new_node