"""
1370. Increasing Decreasing String
https://leetcode.com/problems/increasing-decreasing-string/
"""


class Solution:
    def sortString(self, s: str) -> str:
        result = ''
        front = True

        while s:
            sorted_s = sorted(list(set(s)))
            for i in range(len(sorted_s)):
                if front:
                    s_i = s.index(sorted_s[i])
                else:
                    s_i = s.index(sorted_s[len(sorted_s) - i - 1])
                result += s[s_i]
                s = s[:s_i] + s[s_i+1:]
                if len(s) == 0: break
            if len(s) == 0: break
            front = not front

        return result
