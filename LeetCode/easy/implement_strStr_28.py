"""
28. Implement strStr()
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle) if True else -1




solution = Solution()
print(solution.strStr("hello", "ll"))       # 2
print(solution.strStr("aaaaa", "bba"))      # -1
print(solution.strStr("", ""))              # 0
