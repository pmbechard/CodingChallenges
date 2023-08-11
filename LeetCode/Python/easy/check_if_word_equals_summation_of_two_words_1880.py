"""
1880. Check if Word Equals Summation of Two Words
https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
"""


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        sum_1, sum_2, sum_3 = '', '', ''
        longest = max([len(x) for x in [firstWord, secondWord, targetWord]])
        for i in range(longest):
            if i < len(firstWord):
                sum_1 += str(ord(firstWord[i]) - 97)
            if i < len(secondWord):
                sum_2 += str(ord(secondWord[i]) - 97)
            if i < len(targetWord):
                sum_3 += str(ord(targetWord[i]) - 97)
        return int(sum_1) + int(sum_2) == int(sum_3)
