class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = deque()
        curr_max = -inf
        for i in reversed(range(len(heights))):
            if curr_max < heights[i]:
                res.appendleft(i)
            curr_max = max(curr_max, heights[i])
        
        return list(res)
