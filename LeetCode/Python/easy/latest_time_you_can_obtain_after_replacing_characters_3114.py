"""
3114. Latest Time You Can Obtain After Replacing Characters
https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/
"""


class Solution:
    def findLatestTime(self, s: str) -> str:
        result = ''

        # HOURS
        if s[0] == s[1] == '?':
            result = '11:'
        elif s[0] == '?' and s[1] != '1' and s[1] != '0':
            result = f'0{s[1]}:'
        elif s[0] == '?':
            result = f'1{s[1]}:'
        elif s[1] == '?' and s[0] == '0':
            result = f'{s[0]}9:'
        elif s[1] == '?' and s[0] == '1':
            result = f'{s[0]}1:'
        else:
            result = s[:3]

        # MINUTES
        if s[3] == s[4] == '?':
            return result + '59'
        elif s[3] == '?':
            return result + '5' + s[4]
        elif s[4] == '?':
            return result + s[3] + '9'
        else:
            return result + s[3:]
