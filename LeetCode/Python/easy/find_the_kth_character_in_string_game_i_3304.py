"""
3304. Find the K-th Character in String Game I
https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
"""


class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        while len(word) < k:
            word += [chr(((ord(c) + 1) % 97) + 97) for c in word]
        return word[k - 1]
