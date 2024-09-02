"""
1894. Find the Student that Will Replace the Chalk
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
"""


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k > sum(chalk):
            k = k % sum(chalk)
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i
        return 0
