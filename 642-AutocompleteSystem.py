class Trie:
    def __init__(self):
        self.children = dict()
        self.hot_degree = 0

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.addWord(sentence, time)
        self.cur_node = self.trie
        self.prefix = ""
        
    def addWord(self, sentence, time):
        cur_node = self.trie
        for char in sentence:
            if char not in cur_node.children:
                cur_node.children[char] = Trie()
            cur_node = cur_node.children[char]
        cur_node.hot_degree -= time

    def search_prefix(self, cur_node, cur_prefix, char):
		res = []
		cur_prefix += char
		if cur_node is not None and char in cur_node.children:
			cur_node = cur_node.children[char]
		else:
			return res, cur_prefix, None

		# dfs here
		frontier = [(cur_node, cur_prefix)]
		while frontier:
			expand, word_cur = frontier.pop()
			if expand.hot_degree:
				res.append((expand.hot_degree, word_cur))

			for kid in expand.children:
				frontier.append((expand.children[kid], word_cur + kid))

		sorted_words = list(map(lambda x: x[1], sorted(res)[:3]))
		return sorted_words, cur_prefix, cur_node
    
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.addWord(self.prefix, 1)
            self.prefix = ""
            self.cur_node = self.trie
            return []
        else:
            top_k, self.prefix, self.cur_node = self.search_prefix(self.cur_node, self.prefix, c)
            return top_k


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)