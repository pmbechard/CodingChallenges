"""
151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(re.split('\s+', s.strip())[::-1])
