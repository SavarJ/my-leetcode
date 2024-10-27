class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        small = None
        prev = None
        def solve(node):
            nonlocal small, prev
            if not node: return
            
            solve(node.left)
            if not prev:
                small = node
            else:
                prev.right = node

            node.left = prev
            prev = node

            solve(node.right)
            
            return node
        
        solve(root)
        small.left = prev
        prev.right = small
        return small


        # if not root: return 

        # arr = []
        # def solve(node):
        #     if not node: return None
        #     solve(node.left)
        #     arr.append(node)
        #     solve(node.right)
        
        # solve(root)
        # for i in range(len(arr)):
        #     node = arr[i]
        #     node.left = arr[i-1]
        #     node.right = arr[(i+1)%len(arr)]
        
        # return arr[0]
