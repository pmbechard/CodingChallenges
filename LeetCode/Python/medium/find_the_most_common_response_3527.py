"""
3527. Find the Most Common Response
https://leetcode.com/problems/find-the-most-common-response/
"""


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        r = [x for y in responses for x in set(y)]
        ctr = Counter(r)
        result_word = None
        result_freq = 0
        for word, freq in ctr.items():
            if freq > result_freq or (freq == result_freq and word < result_word):
                result_word = word
                result_freq = freq
        return result_word
