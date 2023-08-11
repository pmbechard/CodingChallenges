"""
2609. Find the Longest Balanced Substring of a Binary String
https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        count = start = 0
        while True:
            index = s.find('01', start)
            if index == -1:
                break
            else:
                new_count = self.get_balanced_from(index, s)
                if new_count > count:
                    count = new_count
            start = index + 1
        return count

    def get_balanced_from(self, index, s):
        current = 2
        l, r = index, index + 1
        while l > 0 and r < len(s):
            l -= 1
            r += 1
            if l < 0 or r == len(s): break
            if s[l] == '0' and s[r] == '1':
                current += 2
            else:
                break
        return current
