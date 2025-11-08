"""
3683. Earliest Time to Finish One Task
https://leetcode.com/problems/earliest-time-to-finish-one-task/
"""


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([sum(task) for task in tasks])
