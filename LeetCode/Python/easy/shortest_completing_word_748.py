"""
748. Shortest Completing Word
https://leetcode.com/problems/shortest-completing-word/
"""


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        filtered = ''.join(sorted([x.lower() for x in licensePlate if x.isalpha()]))
        shortest = None
        for word in words:
            if not shortest or len(word) < len(shortest):
                for letter in set(filtered):
                    if letter not in word or word.count(letter) < filtered.count(letter):
                        break
                else:
                    shortest = word
        return shortest
