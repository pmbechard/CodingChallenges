"""
3163. String Compression III
https://leetcode.com/problems/string-compression-iii/
"""


class Solution:
    def compressedString(self, word: str) -> str:
        prev = [1, word[0]]
        result = ''
        for c in word[1:]:
            if prev[0] == 9 or prev[1] != c:
                result += f'{prev[0]}{prev[1]}'
                prev = [1, c]
            else:
                prev[0] += 1
        return result + f'{prev[0]}{prev[1]}'
