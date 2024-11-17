class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*(len(nums)-k+1)
        streak = 0
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]+1: streak += 1
            else: streak = 1

            if streak >= k:
                res[i-k+1] = nums[i]
        
        return res

        # res = []
        # l = 0
        # prev = nums[0]-1
        # for r in range(len(nums)):
        #     if nums[r] != prev+1:
        #         l = r
            
        #     if r-l+1 >= k:
        #         res.append(nums[r])
        #     elif r+1 >= k:
        #         res.append(-1)
            
        #     prev = nums[r]

        # return res
