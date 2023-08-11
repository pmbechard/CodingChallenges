"""
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for letter in s:
            if not stack or stack[-1] != letter:
                stack.append(letter)
            else:
                stack.pop()
        return ''.join(stack)
