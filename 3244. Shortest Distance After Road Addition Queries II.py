class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for i in range(n):
            g[i].add(i+1)
        
        def bfs():
            queue = deque([(0, 0)]) 
            visit = set()
            while queue:
                node, dist = queue.popleft()
                if node == n-1: return dist
                if node in visit: continue

                visit.add(node)
                for nei in g[node]:
                    queue.append((nei, dist+1))


        res = []
        for a,b in queries:
            g[a].add(b)
            res.append(bfs())
        
        return res
