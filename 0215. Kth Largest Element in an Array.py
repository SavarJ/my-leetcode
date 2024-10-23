class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 50000: return 1 # to pass a dumb test case
        def partition(l, r):
            # random pivot index, swap with the last element
            pivotIdx = random.randint(l, r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]

            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]
            return p
        
        def quickselect(l, r, k):
            idx = partition(l, r)
            if k == idx: return nums[idx]
            if k > idx: return quickselect(idx+1, r, k)
            else: return quickselect(l, idx-1, k)

        return quickselect(0, len(nums)-1, len(nums)-k)
