class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels_to_heights = defaultdict(list)
        node_to_level = {}

        def dfs(node, level):
            if not node: return 0

            left, right = dfs(node.left, level+1), dfs(node.right, level+1)
            height = max(left, right)

            levels_to_heights[level].append((height, node.val))
            levels_to_heights[level] = sorted(levels_to_heights[level])[-2:] # only care about the max 2
            node_to_level[node.val] = level

            return height+1
        
        dfs(root, 0)

        rootHeight = levels_to_heights[0][-1][0]
        res = []

        for node in queries:
            nodeLevel = node_to_level[node]
            levelArr = levels_to_heights[nodeLevel]

            maxHeight, maxNode = levelArr[-1]
            if maxNode != node: # the height won't change since we aren't removing the maxHeight
                res.append(rootHeight)
            else:
                if len(levelArr) > 1: # we are the maxHeight, so pick the second highest
                    res.append(rootHeight-maxHeight+levelArr[-2][0])
                else: # there is no second highest, so the whole level is empty now
                    res.append(nodeLevel-1)
        
        return res
