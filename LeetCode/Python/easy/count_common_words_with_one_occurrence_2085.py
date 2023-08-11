"""
2085. Count Common Words With One Occurrence
https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len([i for i in words1 if words1.count(i) == 1 and words2.count(i) == 1])
