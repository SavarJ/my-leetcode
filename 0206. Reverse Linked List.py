class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        while head:
            nxt, head.next = head.next, dummy
            dummy, head = head, nxt
        return dummy
