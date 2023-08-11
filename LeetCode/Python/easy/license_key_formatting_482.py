"""
482. License Key Formatting
https://leetcode.com/problems/license-key-formatting/
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-')).upper()
        output = ''
        for i in range(len(s), 0, -k):
            output = s[max(0, i - k): i] + '-' + output
        return output[:-1]
