"""
2810. Faulty Keyboard
https://leetcode.com/problems/faulty-keyboard/
"""


class Solution:
    def finalString(self, s: str) -> str:
        result = ''
        for i in s:
            if i == 'i':
                result = result[::-1]
            else:
                result += i
        return result
