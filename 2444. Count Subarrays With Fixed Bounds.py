class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        mini = maxi = badi = -1
        for i in range(len(nums)):
            if nums[i] == minK: mini = i
            if nums[i] == maxK: maxi = i
            if nums[i] < minK or nums[i] > maxK: badi = i
            res += max(0, min(maxi, mini) - badi)

        return res


        # latestMinIdx = None
        # latestMaxIdx = None
        # validSubarrayLeftIdx = 0
        # res = 0

        # for r in range(len(nums)):
        #     currValue = nums[r]

        #     if currValue < minK or currValue > maxK:
        #         validSubarrayLeftIdx = r+1
        #         latestMinIdx = None
        #         latestMaxIdx = None
        #     if currValue == minK:
        #         latestMinIdx = r
        #     if currValue == maxK:
        #         latestMaxIdx = r
            
        #     if latestMinIdx != None and latestMaxIdx != None:
        #         minimumIdx = min(latestMinIdx, latestMaxIdx)
        #         if minimumIdx >= validSubarrayLeftIdx:
        #             res += minimumIdx-validSubarrayLeftIdx+1
        
        # return res
