"""
648. Replace Words
https://leetcode.com/problems/replace-words/
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x: len(x))
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            for root in dictionary:
                if sentence[i].find(root) == 0:
                    sentence[i] = root
                    break
        return ' '.join(sentence)
