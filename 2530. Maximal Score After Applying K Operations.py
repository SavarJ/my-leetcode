class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-val for val in nums]
        heapify(heap)
        return sum(-heapreplace(heap, -ceil(-heap[0]/3)) for _ in range(k))
