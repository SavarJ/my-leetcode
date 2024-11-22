class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter()
        for row in matrix:
            id = tuple([a!=b for a,b in pairwise(row)])
            count[id] += 1
        
        return max(count.values())
