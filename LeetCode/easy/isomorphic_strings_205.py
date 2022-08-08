"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_letters = dict()
        t_letters = dict()
        iso_s = ''
        iso_t = ''
        for i in range(len(s)):
            if s_letters.get(s[i]):
                iso_s += s_letters.get(s[i]) + ','
            else:
                s_letters[s[i]] = str(i)
                iso_s += str(i)
            if t_letters.get(t[i]):
                iso_t += str(t_letters.get(t[i])) + ','
            else:
                iso_t += str(i)
                t_letters[t[i]] = str(i)
        return iso_s == iso_t
