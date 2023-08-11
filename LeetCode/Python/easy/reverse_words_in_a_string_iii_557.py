"""
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        return ' '.join(s_list)
