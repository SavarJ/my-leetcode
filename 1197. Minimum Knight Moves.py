class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        dirs = [-2, -1, 1, 2]

        queue = deque([[0, 0]])
        visit = set()
        visit.add((0, 0))

        moves = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == (x, y): return moves

                for r2, c2 in ((r+i, c+j) for i in dirs for j in dirs if abs(i) != abs(j)):
                    if (r2, c2) not in visit and r2 >= -2 and 2 >= -2:
                        visit.add((r2, c2))
                        queue.append([r2, c2])

            moves += 1
