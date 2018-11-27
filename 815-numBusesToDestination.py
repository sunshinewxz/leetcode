from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        line = defaultdict(set)
        used = set()
        for i,route in enumerate(routes):
            for bus in route:
                line[bus].add(i)
        depth = 0
        stack = [S]
        while(len(stack) > 0):
            stack_len = len(stack)
            for i in range(stack_len):
                node = stack.pop(0)
                if node == T:
                    return depth
                for line_index in line[node]:
                    if line_index not in used:
                        used.add(line_index)
                        for next_bus in routes[line_index]:
                            if next_bus != node:
                                stack.append(next_bus)
            depth += 1
        return -1