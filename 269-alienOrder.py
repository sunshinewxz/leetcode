# better solution
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        relation = []
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(min(len(word1), len(word2))):
                a, b = word1[j], word2[j]
                if a != b:
                    relation.append(a+b)
                    break
        chars = set(''.join(words))
        order = []
        while(len(relation)>0):
            free = chars - set(r[1] for r in relation)
            if len(free) == 0:
                return ''
            order += free
            chars -= free
            relation = [new for new in relation if free.isdisjoint(new)]
        return ''.join(order+list(chars))
                   
        
# original solution
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        node = set()
        if len(words) == 0:
            return ""
        if len(words) == 1:
            return "".join(words[0])
        # get all nodes(char) in the word list
        for word in words:
            for ch in word:
                node.add(ch)
        node_num = len(node)
        # print(node)
        in_degree = {}
        for n in node:
            in_degree[n] = 0
        graph, in_degree = self.constructGraph(words, in_degree)
        node_queue = []
        result = []
        for node in in_degree:
            if in_degree[node] == 0:
                node_queue.append(node)
                result.append(node)
        while(len(node_queue) > 0):
            node_temp = node_queue.pop()
            for sub_node in graph[node_temp]:
                in_degree[sub_node] -= 1
                if in_degree[sub_node] == 0:
                    node_queue.append(sub_node)
                    result.append(sub_node)
        if len(result) == node_num:
            return "".join(result)
        else:
            return ""
            
        
    def constructGraph(self, words, in_degree):
        graph = {}
        # in_degree = {}
        flag = 0
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            length = min(len(word1), len(word2))
            for j in range(length):
                flag = j
                if word1[j] != word2[j]:
                    if word1[j] in graph and word2[j] not in graph[word1[j]]:
                        graph[word1[j]].append(word2[j])
                        in_degree[word2[j]] += 1
                    elif word1[j] not in graph:
                        graph[word1[j]] = [word2[j]]
                        in_degree[word2[j]] += 1
                    if word2[j] not in graph:
                        graph[word2[j]] = []
                    break
                else:
                    if word1[j] not in graph:
                        graph[word1[j]] = []
            for j in range(flag+1, len(word1)):
                if word1[j] not in graph:
                        graph[word1[j]] = []
            for j in range(flag+1, len(word2)):
                if word2[j] not in graph:
                        graph[word2[j]] = []
        return graph, in_degree
        
