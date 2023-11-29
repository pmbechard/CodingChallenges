"""
2375. Construct Smallest Number From DI String
https://leetcode.com/problems/construct-smallest-number-from-di-string/
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        output = list(range(1, len(pattern) + 2))
        i = 0
        while i < len(pattern):
            if pattern[i] == 'D':
                j = i + 1
                while j < len(pattern) and pattern[j] == 'D':
                    j += 1
                output[i:j + 1] = output[i: j + 1][::-1]
                i = j
            i += 1
        return ''.join([str(x) for x in output])
