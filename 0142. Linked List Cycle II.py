class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        again = slow = fast = head
        while True:
            if not fast or not fast.next: return None
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        while slow != again:
            slow, again = slow.next, again.next
        return slow
