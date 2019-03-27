# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        if not k: return head
        
        size = 0
        ite = head
        while ite:
            ite = ite.next
            size += 1
        
        if size == k: return head
        if size < k:
            k = k%size
        c = size - k - 1
        ite = head
        while ite and ite.next and c:
            ite = ite.next
            c -= 1
        
        head2 = ite.next
        if not head2: return head
        ite.next = None
        
        ite2 = head2
        while ite2.next:
            ite2 = ite2.next
        ite2.next = head
        return head2