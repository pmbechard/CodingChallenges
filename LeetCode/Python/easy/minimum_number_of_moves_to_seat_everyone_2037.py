"""
2037. Minimum Number of Moves to Seat Everyone
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        answer = 0
        students.sort()
        seats.sort()
        for i in range(len(students)):
            answer += abs(students[i] - seats[i])
        return answer
