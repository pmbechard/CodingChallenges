"""
551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i/
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and s.find('LLL') == -1
