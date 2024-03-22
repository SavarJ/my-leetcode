class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow = None, slow.next
        dummy = None
        while slow:
            nxt, slow.next = slow.next, dummy
            dummy, slow = slow, nxt
        
        while head and dummy:
            if head.val != dummy.val: return False
            head, dummy = head.next, dummy.next
        return True
