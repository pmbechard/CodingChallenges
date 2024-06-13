"""
3178. Find the Child Who Has the Ball After K Seconds
https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/
"""


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        curr, mov = 0, 1
        for i in range(1, k + 1):
            if curr == n - 1:
                mov = -1
            elif curr == 0:
                mov = 1
            curr += mov
        return curr
