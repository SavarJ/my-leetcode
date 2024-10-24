class Solution:
    def topKFrequent(self, A: List[int], k: int) -> List[int]:
        freq = Counter(A)
        nums = list(freq.keys())

        def partition(l, r):
            pivotIdx = random.randint(l, r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]

            pivot, p = nums[r], 0
            for i in range(r):
                if freq[nums[i]] <= freq[pivot]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p

        def quickselect(l, r, k):
            idx = partition(l, r)
            if k == idx: return nums[idx:]
            if k > idx: return quickselect(idx+1, r, k)
            else: return quickselect(l, idx-1, k)
        
        return quickselect(0, len(nums)-1, len(nums)-k)
