"""
2432. The Employee That Worked on the Longest Task
https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
"""


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        curr = max_time = 0
        max_id = None
        for i in logs:
            time = i[1] - curr
            if (time > max_time) or (time == max_time and i[0] < max_id):
                max_time = time
                max_id = i[0]
            curr = i[1]
        return max_id
