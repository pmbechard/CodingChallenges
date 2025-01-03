"""
3210. Find the Encrypted String
https://leetcode.com/problems/find-the-encrypted-string/
"""


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return ''.join([s[(i + k) % len(s)] for i in range(len(s))])
