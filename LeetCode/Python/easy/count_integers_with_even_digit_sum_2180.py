"""
2180. Count Integers With Even Digit Sum
https://leetcode.com/problems/count-integers-with-even-digit-sum/
"""


class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if sum([int(x) for x in str(i)]) % 2 == 0:
                count += 1
        return count
