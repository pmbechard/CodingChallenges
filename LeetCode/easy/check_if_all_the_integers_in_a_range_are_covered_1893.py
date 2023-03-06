"""
1893. Check if All the Integers in a Range Are Covered
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
"""


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check_set = set(range(left, right + 1))
        ranges_set = set()
        for r in ranges:
            ranges_set.update(range(r[0], r[1] + 1))
        return check_set.issubset(ranges_set)
