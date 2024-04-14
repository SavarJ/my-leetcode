class Node:
    def __init__(self, val=None):
        self.val, self.children, self.hasEnd = val, [None]*26, False

class MagicDictionary:
    def __init__(self):
        self.root = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for c, idx in ((word[i], ord(word[i])%26) for i in range(len(word))):
                node.children[idx] = node.children[idx] or Node(c)
                node = node.children[idx]
            
            node.hasEnd = True
        
    def search(self, searchWord: str) -> bool:
        return self.searchHelper(self.root, searchWord, -1, 1)
    
    def searchHelper(self, node, word, i, wrongCount):
        if i > -1:
            if word[i] != node.val: wrongCount -= 1
            if wrongCount < 0: return False
            if i == len(word)-1: return not wrongCount and node.hasEnd

        return any(self.searchHelper(child, word, i+1, wrongCount) for child in node.children if child)
