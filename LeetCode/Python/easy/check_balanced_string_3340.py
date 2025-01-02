"""
3340. Check Balanced String
https://leetcode.com/problems/check-balanced-string/
"""


class Solution:
    def isBalanced(self, num: str) -> bool:
        count = 0
        for i in range(len(num)):
            count = count + int(num[i]) if i % 2 == 0 else count - int(num[i])
        return count == 0
