from collections import deque
class TRIE:
    def __init__(self):
        self.root = {}

    def add_node(self, word, i):
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}

            if '@' not in node or node['@'][0] > len(word) or (node['@'][0] == len(word) and node['@'][1] > i):
                node['@'] = [len(word), i]

            node = node[ch]

        if '@' not in node or node['@'][0] > len(word) or (node['@'][0] == len(word) and node['@'][1] > i):
                node['@'] = [len(word), i]

    def search(self, word):
        node = self.root
        suffix = ''

        for ch in word:
            if ch not in node:
                break
            suffix += ch
            node = node[ch]

        # find shortest path in node
        return node['@'][1]

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = TRIE()

        for i, word in enumerate(wordsContainer):
            trie.add_node(word[::-1], i)

        res = []
        for word in wordsQuery:
            res.append(trie.search(word[::-1]))

        return res