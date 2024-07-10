"""
1598. Crawler Log Folder
https://leetcode.com/problems/crawler-log-folder/
"""


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dist = 0
        for log in logs:
            if log == '../':
                dist = max(0, dist - 1)
            elif log == './':
                continue
            else:
                dist += 1
        return dist
