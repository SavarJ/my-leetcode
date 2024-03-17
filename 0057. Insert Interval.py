class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in reversed(range(-1, len(intervals))):
            if i == -1: intervals.insert(0, newInterval)
            elif newInterval[0] >= intervals[i][0]:
                intervals.insert(i+1, newInterval)
                break
        
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = stack.pop(), intervals[i]
            stack.extend([a, b] if b[0] > a[1] else [[min(a[0],b[0]), max(a[1],b[1])]])
        
        return stack
