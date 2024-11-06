# class Node:
#     def __init__(self, val=""):
#         self.val = val
#         self.children = {}
#         self.idxes = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        l, r = 0, len(products)-1
        for i, char in enumerate(searchWord):
            while l <= r: # shift both pointers to correct spot
                if i >= len(products[l]) or products[l][i] != char:
                    l += 1
                elif i >= len(products[r]) or products[r][i] != char:
                    r -= 1
                else: # now valid
                    break

            suggestionLength = max(min(3, r-l+1), 0)
            res.append(products[l:l+suggestionLength])
        
        return res
        
        # products.sort()
        # trie = Node()

        # for i, product in enumerate(products):
        #     node = trie
        #     for char in product:
        #         if char not in node.children:
        #             node.children[char] = Node(char)
                
        #         node = node.children[char]
        #         if len(node.idxes) < 3:
        #             node.idxes.append(i)
        
        # res = []
        # node = trie
        # for char in searchWord:
        #     if char not in node.children:
        #         res.append([])
        #         node = Node()
        #         continue
            
        #     node = node.children[char]
        #     res.append([products[idx] for idx in node.idxes])

        # return res
