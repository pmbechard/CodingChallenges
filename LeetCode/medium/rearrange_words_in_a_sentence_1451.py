"""
1451. Rearrange Words in a Sentence
https://leetcode.com/problems/rearrange-words-in-a-sentence/
"""


class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower().split(' ')
        text.sort(key=lambda x: len(x))
        text[0] = text[0].title()
        return ' '.join(text)
