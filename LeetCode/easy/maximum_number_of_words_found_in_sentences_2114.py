"""
2114. Maximum Number of Words Found in Sentences
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
"""

class Solution:
    def mostWordsFound(self, sentences):
        result = 0
        for sentence in sentences:
            current = len(sentence.split(' '))
            if current > result:
                result = current
        return result
