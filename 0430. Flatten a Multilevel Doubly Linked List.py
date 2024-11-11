class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def solve(head):
            node = head
            prev = head
            while node:
                nextNode = node.next
                if node.child:
                    childHead, childTail = solve(node.child)
                    node.child = None

                    node.next = childHead
                    childHead.prev = node
                    childTail.next = nextNode
                    if nextNode:
                        nextNode.prev = childTail
                
                prev = node
                node = node.next

            return head, prev #prev should be the tailw
        
        return solve(head)[0]
