"""
1668. Maximum Repeating Substring
https://leetcode.com/problems/maximum-repeating-substring
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_seq = word * (len(sequence) // len(word))
        count = 0
        while max_seq:
            if max_seq in sequence:
                count += 1
            max_seq = max_seq[len(word):]
        return count
