class Node:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.results = []
        self.idx = -1

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Node()
        self.idxToSentence = {}
        self.freq = Counter()

        for i, sentence in enumerate(sentences):
            self.addSentence(sentence, i)
            self.freq[i] += times[i]
            
        self.curr = []
        self.prevNode = self.trie
    
    def addSentence(self, sentence, idx):
        node = self.trie

        for char in sentence:
            if char not in node.children:
                node.children[char] = Node(char)
            
            node = node.children[char]
            node.results.append(idx)
        
        node.idx = idx
        self.idxToSentence[idx] = sentence

    
    def returnResults(self, node):
        if not node: return []
        idxes = sorted(node.results, key=lambda i: (-self.freq[i], self.idxToSentence[i]))[:3]
        return list(map(self.idxToSentence.get, idxes))

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.curr.append(c)
            node = self.prevNode

            if node and c in node.children:
                node = node.children[c]
                self.prevNode = node
                return self.returnResults(node)
            else:
                self.prevNode = None
                return []
        
        else:
            node = self.prevNode

            if node and node.idx > -1:
                self.freq[node.idx] += 1
            else:
                sentence = ''.join(self.curr)
                idx = len(self.idxToSentence)
                self.addSentence(sentence, idx)
                self.freq[idx] += 1

            self.prevNode = self.trie
            self.curr = []

            return []
