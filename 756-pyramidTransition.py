class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        py_dict = {}
        for al in allowed:
            if al[:2] not in py_dict:
                py_dict[al[:2]] = []
            py_dict[al[:2]].append(al[2])
        
        def dfs(bottom, next_layer):
            if len(bottom) == 1:
                return True
            if bottom[:2] in py_dict:
                for nextElement in py_dict[bottom[:2]]:
                    if len(bottom) <= 2:
                        if dfs(next_layer+nextElement, ''):
                            return True
                    elif len(next_layer) <= 0 or (next_layer[-1]+nextElement) in py_dict:
                        if dfs(bottom[1:], next_layer+nextElement):
                            return True
            return False
        return dfs(bottom, '')