class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]: # new interval finishes before
                return res + [newInterval] + intervals[i:]
            elif newInterval[0] > interval[1]: # new interval starts after
                res.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        return res + [newInterval]
