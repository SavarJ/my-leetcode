class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a%b)
        
        curr = head
        while curr and curr.next:
            node = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr.next = node
            curr = curr.next.next
        
        return head
