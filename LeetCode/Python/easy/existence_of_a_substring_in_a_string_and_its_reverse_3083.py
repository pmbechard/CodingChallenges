"""
3083. Existence of a Substring in a String and Its Reverse
https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse
"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        sub_set = set()
        for i in range(len(s) - 1):
            current = s[i: i + 2]
            sub_set.add(current)
            if current[::-1] in sub_set:
                return True
        return False
