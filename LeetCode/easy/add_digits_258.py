"""
258. Add Digits
https://leetcode.com/problems/add-digits/
"""


class Solution:
    def addDigits(self, num: int) -> int:
        s_num = str(num)
        while len(s_num) > 1:
            s_num = str(sum([int(x) for x in s_num]))
        return int(s_num)
