class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ksum = psum = kl = pl = kres = pres = 0
        K, P = goal, goal-1

        for r in range(len(nums)):
            ksum += nums[r] ; psum += nums[r]

            while kl <= r and ksum > K:
                ksum, kl = ksum-nums[kl], kl+1
            kres += r-kl+1
            
            while pl <= r and psum > P:
                psum, pl = psum-nums[pl], pl+1
            pres += r-pl+1
        
        return kres - pre
