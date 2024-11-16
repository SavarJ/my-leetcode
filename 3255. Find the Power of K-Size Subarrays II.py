class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        prev = nums[0]-1
        for r in range(len(nums)):
            if nums[r] != prev+1:
                l = r
            
            if r-l+1 >= k:
                res.append(nums[r])
            elif r+1 >= k:
                res.append(-1)
            
            prev = nums[r]

        return res 
