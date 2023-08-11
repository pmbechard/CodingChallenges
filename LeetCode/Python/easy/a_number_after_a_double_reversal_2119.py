"""
2119. A Number After a Double Reversal
https://leetcode.com/problems/a-number-after-a-double-reversal/
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if len(str(num)) > 1 and str(num)[-1] == "0":
            return False
        else:
            return True
