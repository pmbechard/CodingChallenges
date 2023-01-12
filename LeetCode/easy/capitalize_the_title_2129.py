"""
2129. Capitalize the Title
https://leetcode.com/problems/capitalize-the-title/
"""


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        word_list = []
        for word in title.split(' '):
            if len(word) > 2:
                word_list.append(word.title())
            else:
                word_list.append(word.lower())
        return ' '.join(word_list)
