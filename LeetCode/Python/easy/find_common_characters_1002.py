"""
1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/
"""
from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # counter = None
        # for word in words:
        #     if counter != None:
        #         counter = counter & Counter(word)
        #     else:
        #         counter = Counter(word)
        # result = []
        # for k in counter:
        #     for i in range(counter[k]):
        #         result.append(k)
        # return result

        return reduce(lambda a, b: a + [b[0]] * b[1],
                      reduce(lambda a, b: Counter(b) & a, words[1:], Counter(words[0])).items(), [])
