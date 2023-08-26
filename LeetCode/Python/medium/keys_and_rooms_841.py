"""
841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        to_visit = {0}
        while to_visit:
            current = to_visit.pop()
            visited.add(current)
            for room in rooms[current]:
                to_visit.add(room)
            to_visit.difference_update(visited)
        return len(visited) == len(rooms)
