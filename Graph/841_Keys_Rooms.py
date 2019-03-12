class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = []
        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.append(room)
                keys = rooms[room]
                for key in keys:
                    if key not in visited:
                        stack.append(key)
        return len(visited) == len(rooms)