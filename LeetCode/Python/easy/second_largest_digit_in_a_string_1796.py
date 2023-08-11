"""
1796. Second Largest Digit in a String
https://leetcode.com/problems/second-largest-digit-in-a-string/
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for letter in s:
            if letter.isnumeric():
                nums.add(int(letter))
        return sorted(nums)[-2] if len(nums) > 1 else -1
