class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = -inf
        curr_min, curr_max = nums[0], nums[0]

        for i in range(len(nums)+1):
            num = 0 if i == len(nums) else nums[i]

            if num.bit_count() == curr_min.bit_count(): # part of same group
                curr_min = min(curr_min, num)
                curr_max = max(curr_max, num)

            else: # num part of different group
                if curr_min < prev_max: return False
                prev_max = curr_max
                curr_min, curr_max = num, num
        
        return True
