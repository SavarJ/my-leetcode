class Solution:
    def numIslands2(self, R: int, C: int, positions: List[List[int]]) -> List[int]:
        def convert(r, c): return r * C + c

        parents = list(range(R*C))

        def find(x):
            if parents[x] != x: parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            parents[find(b)] = find(a)

        lands = set()
        res = []
        count = 0
        for r, c in positions:
            if (r, c) in lands:
                res.append(count)
                continue
            
            lands.add((r, c))
            count += 1

            for r2, c2 in [[r,c+1], [r+1,c], [r,c-1], [r-1,c]]:
                if r2 in range(R) and c2 in range(C) and (r2, c2) in lands:
                    a, b = convert(r, c), convert(r2, c2)
                    
                    if find(a) != find(b): # we are connecting new lands into 1
                        count -= 1

                    union(a, b)
            
            res.append(count)
        
        return res
