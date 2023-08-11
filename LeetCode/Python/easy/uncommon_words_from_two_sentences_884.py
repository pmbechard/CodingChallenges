"""
884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_list = (s1 + ' ' + s2).split(' ')
        return [x for x in word_list if word_list.count(x) == 1]
