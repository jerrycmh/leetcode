import heapq
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        
        free_room = []
        
        for obj in intervals:
            start, end = obj.start, obj.end
            if not free_room:
                heapq.heappush(free_room, end)
            else:
                if free_room[0] <= start:
                    heapq.heappop(free_room)
                heapq.heappush(free_room, end)
        
        return len(free_room)