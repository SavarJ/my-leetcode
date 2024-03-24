class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = again = fast = 0
        while slow == 0 or slow != fast: slow, fast = nums[slow], nums[nums[fast]]
        while slow != again: slow, again = nums[slow], nums[again]
        return again
