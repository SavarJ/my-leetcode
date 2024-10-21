class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            node = Node(curr.val, curr.next)
            curr.next = node
            curr = curr.next.next
        
        dummy = dummy2 = Node(-1)
        curr = head
        while curr:
            dummy.next = curr.next
            node = dummy.next
            nxt = node.next

            node.random = None if not curr.random else curr.random.next
            node.next = None if not nxt else nxt.next

            curr = nxt
            dummy = dummy.next
        
        return dummy2.next
        
        # m = {None: None}
        # curr = head
        # while curr:
        #     m[curr] = Node(curr.val)
        #     curr = curr.next
        
        # curr = head
        # dummy = Node(-1)
        # while curr:
        #     dummy.next = m[curr]
        #     copy = dummy.next
        #     copy.next = m[curr.next]
        #     copy.random = m[curr.random]

        #     dummy = dummy.next
        #     curr = curr.next
        
        # return m[head]
