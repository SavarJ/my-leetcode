class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: slow, fast = slow.next, fast.next.next
        
        dummy = None
        while slow: slow.next, dummy, slow = dummy, slow, slow.next
        
        curr = head
        while curr and dummy:
            curr.next, curr = dummy, curr.next
            dummy.next, dummy = curr, dummy.next
        
        return head
