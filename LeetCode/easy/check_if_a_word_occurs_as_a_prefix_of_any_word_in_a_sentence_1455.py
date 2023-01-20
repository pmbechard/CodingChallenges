"""
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_list = sentence.split(' ')
        for i in range(len(word_list)):
            if word_list[i].find(searchWord) == 0:
                return i + 1
        return -1
