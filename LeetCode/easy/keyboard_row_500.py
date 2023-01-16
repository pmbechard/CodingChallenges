"""
500. Keyboard Row
https://leetcode.com/problems/keyboard-row/
"""


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        results = []
        for word in words:
            if all([i.lower() in 'qwertyuiop' for i in word]) or all([i.lower() in 'asdfghjkl' for i in word]) or all([i.lower() in 'zxcvbnm' for i in word]):
                results.append(word)
        return results
