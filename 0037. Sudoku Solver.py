class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        options = list(map(str,range(1,10)))

        rows = {r: set() for r in range(R)}
        cols = {c: set() for c in range(C)}
        grid = {(r,c):set() for r in range(3) for c in range(3)}

        def addNum(r, c, num):
            rows[r].add(num)
            cols[c].add(num)
            grid[(r//3,c//3)].add(num)
            board[r][c] = num
        
        def removeNum(r, c, num):
            rows[r].remove(num)
            cols[c].remove(num)
            grid[(r//3,c//3)].remove(num)
            board[r][c] = "."

        for r in range(R):
            for c in range(C):
                cell = board[r][c]
                if cell != ".":
                    addNum(r, c, cell)

        def getValidOptions(r, c):
            for num in options:
                if num not in rows[r] and num not in cols[c] and num not in grid[(r//3,c//3)]:
                    yield num


        def solve(r, c):
            if r == R: return True

            # moving left to right, top to bottom
            c2 = (c+1)%C
            r2 = r + ((c+1)//C)

            if board[r][c] != ".":
                return solve(r2, c2)
            else:
                for num in getValidOptions(r, c):
                    addNum(r, c, num)
                    if solve(r2, c2): return True
                    removeNum(r, c, num)
        
        solve(0, 0)
