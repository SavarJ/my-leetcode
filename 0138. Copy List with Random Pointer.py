class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next, curr = copy, curr.next

        curr = head
        while curr:
            curr.next.random, curr = curr.random.next if curr.random else None, curr.next.next
        
        new, front, old = head, head.next, head.next
        while new:
            newnext, oldnext = new.next.next, old.next.next if old.next else None
            new.next, old.next, new, old = newnext, oldnext, newnext, oldnext
        
        return front
