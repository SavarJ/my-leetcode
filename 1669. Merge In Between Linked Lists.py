class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        x, y = list1, list1
        for i in range(b+1):
            if i == a-1: x = y
            y = y.next
        x.next = list2
        while list2.next: list2 = list2.next
        list2.next = y
        return list1
