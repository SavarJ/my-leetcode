class Node:
    def __init__(self, letter=""):
        self.letter = letter
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.trie = Node()

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            
            node = node.children[char]
        
        node.end = True
        

    def search(self, word: str) -> bool:
        def _searchHelper(i, node):
            if i == len(word):
                return node.end
            
            char = word[i]
            if char != ".":
                return char in node.children and _searchHelper(i+1, node.children[char])
            else:
                return any(_searchHelper(i+1, node) for node in node.children.values())
            

        return _searchHelper(0, self.trie)
