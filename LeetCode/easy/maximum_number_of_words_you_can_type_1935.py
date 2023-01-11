"""
1935. Maximum Number of Words You Can Type
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word_list = text.split(' ')
        result = len(word_list)
        for word in word_list:
            result -= 1 if any([x for x in brokenLetters if word.find(x) > -1]) else 0
        return result
