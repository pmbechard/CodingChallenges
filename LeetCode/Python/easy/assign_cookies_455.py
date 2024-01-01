"""
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        s_i = 0
        for g_i in g:
            if g_i <= s[s_i]:
                s_i += 1
                if s_i == len(s):
                    break
        return s_i
