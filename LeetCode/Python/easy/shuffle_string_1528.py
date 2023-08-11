"""
1528. Shuffle String
https://leetcode.com/problems/shuffle-string/
"""


class Solution:
    def restoreString(self, s, indices):
        result = ""
        for i in range(max(indices) + 1):
            result += s[indices.index(i)]
        return result
