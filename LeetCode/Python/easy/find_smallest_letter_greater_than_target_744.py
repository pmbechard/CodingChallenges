"""
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        options = sorted([x for x in letters if x > target])
        if len(options) > 0: return options[0]
        return letters[0]
