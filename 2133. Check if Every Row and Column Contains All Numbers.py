class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for r in range(len(matrix)):
            row, col = set(), set()
            for c in range(len(matrix)):
                if matrix[r][c] in row or matrix[c][r] in col: return False
                row.add(matrix[r][c]), col.add(matrix[c][r])
        
        return True
