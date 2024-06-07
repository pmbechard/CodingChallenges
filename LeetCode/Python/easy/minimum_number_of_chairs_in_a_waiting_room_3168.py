"""
3168. Minimum Number of Chairs in a Waiting Room
https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/
"""


class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chairs = curr_chairs = 0
        for c in s:
            if c == 'E':
                curr_chairs += 1
                max_chairs = max(max_chairs, curr_chairs)
            else:
                curr_chairs -= 1
        return max_chairs
