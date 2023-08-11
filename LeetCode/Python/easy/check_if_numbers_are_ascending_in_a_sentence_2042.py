"""
2042. Check if Numbers Are Ascending in a Sentence
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/
"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(i) for i in s.split(' ') if i.isnumeric()]
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
