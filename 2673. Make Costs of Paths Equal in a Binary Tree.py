class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        def solve(node):
            nonlocal res
            if node-1 >= n: return 0

            left, right = solve(node*2), solve(node*2+1)
            res += abs(left-right)
            return cost[node-1] + max(left, right)
        
        solve(1)
        return res
