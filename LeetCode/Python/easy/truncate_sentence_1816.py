"""
1816. Truncate Sentence
https://leetcode.com/problems/truncate-sentence/
"""


class Solution:
    def truncateSentence(self, s, k):
        return ' '.join(s.split(' ')[:k])
