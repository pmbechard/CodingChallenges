"""
2545. Sort the Students by Their Kth Score
https://leetcode.com/problems/sort-the-students-by-their-kth-score/
"""


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return sorted(score, reverse=True, key=lambda x: x[k])
