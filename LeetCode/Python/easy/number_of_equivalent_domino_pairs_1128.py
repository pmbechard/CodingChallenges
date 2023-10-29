"""
1128. Number of Equivalent Domino Pairs
https://leetcode.com/problems/number-of-equivalent-domino-pairs/
"""


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freqs = dict()
        for i in dominoes:
            i = tuple(i if i[0] < i[1] else [i[1], i[0]])
            freqs[i] = freqs.get(i, 0) + 1
        output = 0
        for n in freqs.values():
            if n > 1:
                output += (n * (n - 1)) // 2
        return output
