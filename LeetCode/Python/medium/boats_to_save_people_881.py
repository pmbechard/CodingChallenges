"""
881. Boats to Save People
https://leetcode.com/problems/boats-to-save-people
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if left != right and people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
