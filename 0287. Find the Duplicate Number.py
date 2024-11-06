class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i,n in enumerate(nums[1:]):
        #     if n == nums[i]:
        #         return n

        slow = again = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break

        while slow != again: 
            slow, again = nums[slow], nums[again]
            
        return again
