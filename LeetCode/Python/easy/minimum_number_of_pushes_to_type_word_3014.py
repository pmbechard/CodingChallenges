"""
3014. Minimum Number of Pushes to Type Word I
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_count = push_count = 0
        used = dict()
        for letter in word:
            if letter in used:
                push_count += used[letter]
            else:
                letter_count += 1
                used[letter] = ((letter_count - 1) // 8) + 1
                push_count += ((letter_count - 1) // 8) + 1
        return push_count
