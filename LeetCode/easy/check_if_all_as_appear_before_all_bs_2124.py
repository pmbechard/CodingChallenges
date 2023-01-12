"""
2124. Check if All A's Appears Before All B's
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
"""


class Solution:
    def checkString(self, s: str) -> bool:
        first_b = s.find('b')
        last_a = len(s) - s[::-1].find('a') - 1
        if first_b == -1 or s.find('a') == -1:
            return True
        return first_b > last_a
