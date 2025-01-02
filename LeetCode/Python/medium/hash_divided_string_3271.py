"""
3271. Hash Divided String
https://leetcode.com/problems/hash-divided-string/
"""


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ''
        ords = [ord(s[i]) - 97 for i in range(len(s))]
        i = 0
        while i < len(s):
            result += chr(97 + (sum(ords[i: i + k]) % 26))
            i += k
        return result
