# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNum(node):
            res = 0
            power = 1
            while node:
                res += node.val*power
                power *= 10
                node = node.next
            
            return res
        
        total = getNum(l1)+getNum(l2)
        if total == 0: return ListNode(0)
        
        head = ListNode(0)
        node = head
        while total:
            node.next = ListNode(total%10)
            node = node.next
            total //= 10
        
        return head.next
