class Node:
    def __init__(self, val=""):
        self.val = val
        self.children = {}
        self.end = None
        self.count = 0

class Solution:
    def findWords(self, grid: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []
        trie = Node()

        cycle = set()
        def dfs(r, c, node):
            if (r, c) in cycle: return
            if grid[r][c] != node.val: return

            if node.end: 
                res.append(node.end)
                remove(node.end)
                node.end = None

            cycle.add((r, c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr in range(R) and nc in range(C) and grid[nr][nc] in node.children:
                    dfs(nr, nc, node.children[grid[nr][nc]])
            
            cycle.remove((r, c))

        def remove(word):
            node = trie
            for c in word:
                node = node.children[c]
                node.count -= 1
                if node.count == 0:
                    del node
                    break
                
        for word in words:
            node = trie
            for c in word:
                if c not in node.children:
                    node.children[c] = Node(c)
                
                node = node.children[c]
                node.count += 1
            
            node.end = word

        for r in range(R):
            for c in range(C):
                if grid[r][c] in trie.children: 
                    dfs(r, c, trie.children[grid[r][c]])
        
        return res
