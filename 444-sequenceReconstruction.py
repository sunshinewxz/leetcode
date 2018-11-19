from collections import *
class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        incoming = defaultdict(int)
        nodes = set()
        for arr in seqs:
            nodes |= set(arr)
            for i in range(len(arr)):
                if i == 0:
                    incoming[arr[i]] += 0
                if i < len(arr)-1:
                    incoming[arr[i+1]] += 1
                    graph[arr[i]].append(arr[i+1])
        zero_indegree = [key for key in incoming if incoming[key] == 0]
        result = []
        while(len(zero_indegree) == 1):
            node = zero_indegree.pop()
            result.append(node)
            for next_node in graph[node]:
                incoming[next_node] -= 1
                if incoming[next_node] == 0:
                    zero_indegree.append(next_node)
        if len(zero_indegree) > 1:
            return False
        # print(result)
        return len(result) == len(nodes) and result == org

            