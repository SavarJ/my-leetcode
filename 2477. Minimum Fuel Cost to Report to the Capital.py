class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g, self.totalFuel = defaultdict(set), 0
        list(map(lambda r: (g[r[0]].add(r[1]), g[r[1]].add(r[0])), roads))

        def dfs(city, parent):
            people = sum(dfs(n, city) for n in g[city] if n != parent) +1
            if city != 0: self.totalFuel += ceil(people/seats)
            return people

        return (dfs(0, None), self.totalFuel)[1]
