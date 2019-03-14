import heapq
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        heap = []
        while head:
            heapq.heappush(heap, head.val)
            head = head.next
        result = ListNode(heapq.heappop(heap))
        ite = result
        while heap:
            ite.next = ListNode(heapq.heappop(heap))
            ite = ite.next
        return result