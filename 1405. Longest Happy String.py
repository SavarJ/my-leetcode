class Solution:
    def longestDiverseString(self, A: int, B: int, C: int) -> str:
        heap = [(-count, char) for count, char in [(A, "a"), (B, "b"), (C, "c")] if count > 0]
        heapify(heap)
        
        res = []
        while heap:
            count, char = heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap: break

                count2, char2 = heappop(heap)
                res.append(char2)
                if count2+1 != 0:
                    heappush(heap, (count2+1, char2))
            else:
                res.append(char)
                count += 1
            
            if count != 0:
                heappush(heap, (count, char))
        
        return ''.join(res)
