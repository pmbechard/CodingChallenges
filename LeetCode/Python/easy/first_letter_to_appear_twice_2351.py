"""
2351. First Letter to Appear Twice
https://leetcode.com/problems/first-letter-to-appear-twice/
"""


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        checked = []
        for letter in s:
            if letter in checked:
                return letter
            checked.append(letter)
