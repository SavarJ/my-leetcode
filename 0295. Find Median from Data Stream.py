class MedianFinder:
    def __init__(self):
        self.left = [] #maxheap
        self.right = [] #minheap

    def addNum(self, num: int) -> None:
        # always add to the left first
        heappush(self.left, -num)

        # if left side is bigger than right side
        if self.left and self.right and -self.left[0] > self.right[0]:
            heappush(self.right, -heappop(self.left))

        # balance the heaps and ensure len(left) >= len(right)
        if len(self.left) - len(self.right) > 1:
            heappush(self.right, -heappop(self.left))
        
        if len(self.right) - len(self.left) > 0:
            heappush(self.left, -heappop(self.right))

    def findMedian(self) -> float:
        # left heap length should always be equal or greater than right
        if len(self.left) > len(self.right):
            return -self.left[0]
        else: 
            return (-self.left[0]+self.right[0])/2
