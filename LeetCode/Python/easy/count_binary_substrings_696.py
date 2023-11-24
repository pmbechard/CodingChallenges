"""
696. Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_count = curr_count = output = 0
        curr_digit = ''

        for digit in s:
            if digit == curr_digit:
                curr_count += 1
            else:
                prev_count = curr_count
                curr_count = 1
                curr_digit = digit
            if curr_count <= prev_count:
                output += 1
        return output
