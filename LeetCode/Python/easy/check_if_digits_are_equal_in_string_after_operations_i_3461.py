"""
3461. Check If Digits Are Equal in String After Operations I
https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
"""


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while True:
            output = []
            for i in range(len(s) - 1):
                output.append((int(s[i]) + int(s[i + 1])) % 10)
            s = output
            if len(output) == 2:
                break
        return output[0] == output[1]
