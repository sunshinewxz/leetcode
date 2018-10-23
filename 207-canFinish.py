class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 1:
            return True
        while (True):
            mark = [True for i in range(numCourses)]
            delete = 0
            for p in prerequisites:
                mark[p[0]] = False
            for p in prerequisites:
                if mark[p[1]] == True:
                    delete = 1
                    prerequisites.remove(p)
            if len(prerequisites) == 0:
                return True
            if delete == 0:
                return False

                
# better solution 2
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses <= 1:
            return True
        cou_num = 0
        in_degree = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        node_queue = []
        for p in prerequisites:
            in_degree[p[0]] += 1
            graph[p[1]].append(p[0])
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                cou_num += 1
                node_queue.append(i)
        
        while(len(node_queue) > 0):
            node = node_queue.pop()
            for sub_node in graph[node]:
                in_degree[sub_node] -= 1
                if in_degree[sub_node] == 0:
                    cou_num += 1
                    node_queue.append(sub_node)
        if cou_num == numCourses:
            return True
        else:
            return False
                
