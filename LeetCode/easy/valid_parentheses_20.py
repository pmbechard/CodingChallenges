"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s):
        for i in range(len(s) - 1):
            if (s[i] == '(' and s[i + 1] == ')') \
                    or (s[i] == '[' and s[i + 1] == ']') \
                    or (s[i] == '{' and s[i + 1] == '}'):
                if len(s) == 2:
                    return True
                return self.isValid(s[:i] + s[i + 2:])
            elif len(s) == 2:
                return False


solution = Solution()
print(solution.isValid("()"))      # true
print(solution.isValid("()[]{}"))  # true
print(solution.isValid("(]"))      # false
print(solution.isValid("{[]}"))      # true
