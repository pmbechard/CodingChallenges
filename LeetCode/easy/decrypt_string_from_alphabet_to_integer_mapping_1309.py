"""
1309. Decrypt String from Alphabet to Integer Mapping
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        index = 0
        result = ''
        while True:
            if index >= len(s):
                return result
            if index + 2 < len(s) and s[index + 2] == '#':
                result += chr(int(s[index:index+2]) + 96)
                index += 3
            else:
                result += chr(int(s[index]) + 96)
                index += 1
