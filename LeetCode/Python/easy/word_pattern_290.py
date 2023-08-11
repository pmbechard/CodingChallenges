"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = dict()
        pattern_translation = ''
        pattern_counter = 0
        for letter in pattern:
            if pattern_dict.get(letter):
                pattern_translation += pattern_dict.get(letter)
            else:
                pattern_dict[letter] = str(pattern_counter)
                pattern_translation += str(pattern_counter) + ','
                pattern_counter += 1

        s_dict = dict()
        s_translation = ''
        s_counter = 0
        for word in s.split(' '):
            if s_dict.get(word):
                s_translation += s_dict.get(word)
            else:
                s_dict[word] = str(s_counter)
                s_translation += str(s_counter) + ','
                s_counter += 1

        return pattern_translation == s_translation
