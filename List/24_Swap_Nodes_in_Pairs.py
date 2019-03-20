# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        n1, n2 = head, head.next
        prev = None
        
        while n1 and n2:
            if not prev:
                head = n2
            else:
                prev.next = n2
            n1.next = n2.next
            n2.next = n1
            prev = n1
            
            n1 = n1.next
            if n1: n2 = n1.next
        
        return head