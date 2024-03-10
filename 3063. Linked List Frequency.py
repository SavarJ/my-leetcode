# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq, node = defaultdict(int), head
        while node:
            freq[node.val] += 1
            node = node.next
        
        node = dummy = ListNode()
        for val in freq.values():
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return node.next
