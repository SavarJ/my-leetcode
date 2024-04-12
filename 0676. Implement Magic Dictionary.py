class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = [None]*26
        self.hasEnd = False

class MagicDictionary:
    def __init__(self):
        self.root = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.insertToTrie(self.root, list(word)[::-1])
        
    def insertToTrie(self, node, word):
        if not word: 
            node.hasEnd = True
            return
        letter = word.pop()
        idx = ord(letter)%26
        if not node.children[idx]:
            node.children[idx] = Node(letter)
        
        self.insertToTrie(node.children[idx], word)
        

    def search(self, searchWord: str) -> bool:
        return any(self.searchHelper(child, searchWord, 0, 1) for child in self.root.children if child)
    
    def searchHelper(self, node, word, i, wrongCount):
        if word[i] != node.val: wrongCount -= 1
        if wrongCount < 0: return False
        if i == len(word)-1: return wrongCount == 0 and node.hasEnd

        return any(self.searchHelper(child, word, i+1, wrongCount) for child in node.children if child)
