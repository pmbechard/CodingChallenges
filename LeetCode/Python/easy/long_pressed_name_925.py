"""
925. Long Pressed Name
https://leetcode.com/problems/long-pressed-name/
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_idx = typed_idx = 0

        while name_idx < len(name) and typed_idx < len(typed):

            if name[name_idx] != typed[typed_idx]:
                return False

            letter_count = 1
            while name_idx + letter_count < len(name) and name[name_idx] == name[name_idx + letter_count]:
                letter_count += 1

            typed_count = 1
            while typed_idx + typed_count < len(typed) and typed[typed_idx] == typed[typed_idx + typed_count]:
                typed_count += 1

            if typed_count < letter_count:
                return False

            name_idx += letter_count
            typed_idx += typed_count

        while typed_idx < len(typed):
            if typed[typed_idx] != name[-1]:
                return False
            typed_idx += 1

        if name_idx < len(name):
            return False

        return True
