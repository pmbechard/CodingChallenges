"""
2828. Check if a String Is an Acronym of Words
https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/
"""


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
        return True
