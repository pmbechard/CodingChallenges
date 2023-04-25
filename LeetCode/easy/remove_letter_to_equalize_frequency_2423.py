"""
2423. Remove Letter To Equalize Frequency
https://leetcode.com/problems/remove-letter-to-equalize-frequency/
"""


class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            temp = word[:i] + word[i + 1:]
            if len(set([temp.count(j) for j in set(temp)])) == 1:
                return True
        return False
