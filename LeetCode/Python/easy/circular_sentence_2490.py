"""
2490. Circular Sentence
https://leetcode.com/problems/circular-sentence/
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        word_list = sentence.split(' ')
        if len(word_list) == 1: return word_list[0][0] == word_list[0][-1]
        for i in range(len(word_list) - 1):
            if word_list[i][0] != word_list[i - 1][-1] or word_list[i][-1] != word_list[i + 1][0]:
                return False
        return True
