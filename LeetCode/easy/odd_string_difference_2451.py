"""
2451. Odd String Difference
https://leetcode.com/problems/odd-string-difference/
"""


class Solution:
    def oddString(self, words: List[str]) -> str:
        vals = [([ord(letter) - 97 for letter in word], word) for word in words]
        diffs = [([val[0][i + 1] - val[0][i] for i in range(len(val[0]) - 1)], val[1]) for val in vals]

        for i in range(1, len(diffs) - 1):
            left = diffs[i - 1]
            centre = diffs[i]
            right = diffs[i + 1]

            if left[0] == centre[0] and left[0] != right[0]:
                return right[1]
            elif left[0] == right[0] and left[0] != centre[0]:
                return centre[1]
            elif centre[0] == right[0] and centre[0] != left[0]:
                return left[1]
