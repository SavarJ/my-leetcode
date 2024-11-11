class Solution:
    def arraysIntersection(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        arr = [A, B, C]
        res = []
        heap = []
        for i, array in enumerate(arr):
            heappush(heap, [array[0], 0, i])
        k = 3

        while len(heap) == k:
            # check if all elements are the same
            count = 0
            for num, idx, lst in heap:
                if num != heap[0][0]:
                    break
                count += 1
            
            if count == k:
                res.append(heap[0][0])
            
            # increment the lowest idx if possible
            num, idx, lst = heappop(heap)
            if idx+1 < len(arr[lst]):
                heappush(heap, [arr[lst][idx+1], idx+1, lst])
        
        return res
