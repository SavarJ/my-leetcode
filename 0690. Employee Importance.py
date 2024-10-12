class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        g = {e.id:e for e in employees}
        def solve(id):
            return g[id].importance + sum(solve(sub) for sub in g[id].subordinates)
        
        return solve(id)
