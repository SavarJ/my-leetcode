class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        adjList = {i:[] for i in range(-1, nodes)}
        for i, par in enumerate(parent): adjList[par].append(i)
        
        def dfs(node):
            total, size = value[node], 1
            for child in adjList[node]:
                tot, length = dfs(child)
                total, size = total+tot, size+length
            return total, size if total else 0

        return dfs(0)[1]
