class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        return all(b[0] >= a[1] for a, b in pairwise(sorted(intervals)))
