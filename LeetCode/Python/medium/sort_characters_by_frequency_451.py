"""
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        dic = dict()
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        return ''.join([i[0] * i[1] for i in sorted(dic.items(), key=lambda x: -x[1])])
