class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        K, P = k, k-1
        Kres = Kl = Pres = Pl = 0
        Kwindow, Pwindow = Counter(), Counter()

        for r in range(len(nums)):
            Kwindow[nums[r]]+=1
            while len(Kwindow) > K:
                Kwindow[nums[Kl]] -= 1
                if Kwindow[nums[Kl]] == 0: del Kwindow[nums[Kl]]
                Kl += 1
            Kres += r-Kl+1

            Pwindow[nums[r]]+=1
            while len(Pwindow) > P:
                Pwindow[nums[Pl]] -= 1
                if Pwindow[nums[Pl]] == 0: del Pwindow[nums[Pl]]
                Pl += 1
            Pres += r-Pl+1
            
        return Kres-Pres

        # res = far = near = 0
        # window = Counter()
        # for r in range(len(nums)):
        #     window[nums[r]] += 1

        #     while len(window) > k:
        #         window[nums[near]] -= 1
        #         if window[nums[near]] == 0: del window[nums[near]]
        #         near, far = near+1, near+1

        #     while window[nums[near]] > 1:
        #         window[nums[near]] -= 1
        #         near += 1

        #     if len(window) == k:
        #         res += near-far+1

        # return res
