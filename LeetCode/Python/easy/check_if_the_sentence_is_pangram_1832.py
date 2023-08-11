"""
1832. Check if the Sentence Is Pangram
https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ascii_val = 97
        while ascii_val < 123:
            if not chr(ascii_val) in sentence:
                return False
            ascii_val += 1
        return True
