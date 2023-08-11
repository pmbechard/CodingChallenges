"""
1078. Occurrences After Bigram
https://leetcode.com/problems/occurrences-after-bigram/
"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(' ')
        return [text[i] for i in range(len(text)) if i > 1 and text[i-2] == first and text[i-1] == second]
