class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return len(set((inf if b[0]-a[0] == 0 else (b[1]-a[1])/(a[0]-b[0]) for a, b in pairwise(coordinates)))) == 1
