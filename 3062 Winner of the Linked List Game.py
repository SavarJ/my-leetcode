# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even, odd = head, head.next
        count = 0
        while True:
            count += 1 if even.val > odd.val else -1
            if not odd.next: break
            even, odd = even.next.next, odd.next.next
        
        return "Even" if count > 0 else ("Tie" if count == 0 else "Odd")
