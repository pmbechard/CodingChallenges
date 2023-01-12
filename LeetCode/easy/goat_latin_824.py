"""
824. Goat Latin
https://leetcode.com/problems/goat-latin/
"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence_list = sentence.split(' ')
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(sentence_list)):
            if sentence_list[i][0].lower() in vowels:
                sentence_list[i] += 'ma'
            else:
                sentence_list[i] = sentence_list[i][1:] + sentence_list[i][0] + 'ma'
            sentence_list[i] += 'a' * (i + 1)
        return ' '.join(sentence_list)
