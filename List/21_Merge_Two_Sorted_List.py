# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return None
        if not l1: return l2
        if not l2: return l1
        
        head = ListNode(0)
        ite = head
        while l1 and l2:
            if l1.val > l2.val:
                ite.next = l2
                ite = ite.next
                l2 = l2.next
            else:
                ite.next = l1
                ite = ite.next
                l1 = l1.next
        ite.next = l1 or l2
        
        return head.next