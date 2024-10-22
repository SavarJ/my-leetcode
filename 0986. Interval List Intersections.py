class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            aStart, aEnd = A[i]
            bStart, bEnd = B[j]

            s, e = max(aStart, bStart), min(aEnd, bEnd)

            if e-s >= 0:
                res.append((s, e))
            
            if aEnd < bEnd:
                i += 1
            else:
                j += 1

        return res
