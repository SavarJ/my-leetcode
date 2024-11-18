class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = [(c, p) for c, p in zip(capital, profits)]
        heapify(minheap)

        maxheap = []
        for i in range(k):
            while minheap and minheap[0][0] <= w:
                c, p = heappop(minheap)
                heappush(maxheap, -p)
            
            if maxheap:
                w += -heappop(maxheap)
        
        return w
