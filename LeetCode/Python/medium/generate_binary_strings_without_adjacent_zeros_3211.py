"""
3211. Generate Binary Strings Without Adjacent Zeros
https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/
"""


class Solution:
    def __init__(self):
        self.output = []

    def validStrings(self, n: int) -> List[str]:
        self.recurse('0', n)
        self.recurse('1', n)
        return self.output

    def recurse(self, s, length):
        if len(s) == length:
            self.output.append(s)
            return
        if s[-1] == '0':
            self.recurse(s + '1', length)
        if s[-1] == '1':
            self.recurse(s + '0', length)
        if s[-1] == '1':
            self.recurse(s + '1', length)
