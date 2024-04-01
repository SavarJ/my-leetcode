class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        if R*C < len(word): return False
        freq=Counter()
        for r in range(R):
            for c in range(C):
                freq[board[r][c]]+=1
        if freq[word[-1]] < freq[word[0]]: word = word[::-1]

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(r, c, i):
            if r not in range(R) or c not in range(C) or board[r][c] != word[i]: return False
            if i == len(word)-1: return True
            temp, board[r][c] = board[r][c], -1
            found = any(dfs(r+nr, c+nc, i+1) for nr, nc in directions)
            board[r][c] = temp
            return found
            
        return any(dfs(r, c, 0) for r in range(R) for c in range(C) if board[r][c] == word[0])
