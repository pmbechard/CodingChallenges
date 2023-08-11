"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s):
        s = s.replace(" ", "")
        s = s.lower()
        left_index = 0
        right_index = len(s) - 1
        while True:
            if not s or left_index == right_index or (left_index == right_index - 1 and s[left_index] == s[right_index]):
                return True

            if not s[left_index].isalnum():
                left_index += 1
                continue
            if not s[right_index].isalnum():
                right_index -= 1
                continue

            if not s[left_index] == s[right_index]:
                return False
            else:
                left_index += 1
                right_index -= 1
