"""
806. Number of Lines To Write String
https://leetcode.com/problems/number-of-lines-to-write-string/
"""


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        width = 0
        result = [[]]
        for letter in s:
            if width + widths[ord(letter) - 97] <= 100:
                result[-1] += letter
                width += widths[ord(letter) - 97]
            else:
                result.append(letter)
                width = widths[ord(letter) - 97]
        return [len(result), width]
