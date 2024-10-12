class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # arr = [0]*(10**6+2)
        # for s, e in intervals:
        #     arr[s] += 1
        #     arr[e+1] -= 1
        # return max(accumulate(arr))
        d = Counter()
        for s, e in intervals:
            d[s] += 1
            d[e+1] -= 1
        return max(accumulate(val for key, val in sorted(d.items())))
