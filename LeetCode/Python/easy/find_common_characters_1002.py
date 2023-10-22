"""
1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/
"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = None
        for word in words:
            if counter != None:
                counter = counter & Counter(word)
            else:
                counter = Counter(word)
        result = []
        for k in counter:
            for i in range(counter[k]):
                result.append(k)
        return result
