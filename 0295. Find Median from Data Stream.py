class MedianFinder:
    def __init__(self):
        self.heaps = [], [] # left-half is maxheap, right-half is minheap

    def addNum(self, num: int) -> None:
        left, right = self.heaps

        # exchange with right to find the correct, new "lesser" value and push to leftheap
        heappush(left, -heappushpop(right, num))

        # balance the heaps and ensure len(left) >= len(right)
        if len(left) - len(right) > 1:
            heappush(right, -heappop(left))
        
    def findMedian(self) -> float:
        # left heap length should always be equal or greater than right
        left, right = self.heaps
        return -left[0] if len(left) > len(right) else (-left[0]+right[0])/2

# class MedianFinder:
#     def __init__(self):
#         self.heaps = [], [] # left-half is maxheap, right-half is minheap

#     def addNum(self, num: int) -> None:
#         left, right = self.heaps

#         # always add to the left first
#         heappush(left, -num)

#         # if left side is bigger than right side
#         if left and right and -left[0] > right[0]:
#             heappush(right, -heappop(left))

#         # balance the heaps and ensure len(left) >= len(right)
#         if len(left) - len(right) > 1:
#             heappush(right, -heappop(left))
        
#         if len(right) - len(left) > 0:
#             heappush(left, -heappop(right))

#     def findMedian(self) -> float:
#         left, right = self.heaps

#         # left heap length should always be equal or greater than right
#         if len(left) > len(right):
#             return -left[0]
#         else: 
#             return (-left[0]+right[0])/2
