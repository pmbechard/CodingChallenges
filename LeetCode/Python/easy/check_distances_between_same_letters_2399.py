"""
2399. Check Distances Between Same Letters
https://leetcode.com/problems/check-distances-between-same-letters/
"""


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dis_dic = {}
        for i in range(len(s)):
            letter = s[i]
            dis_dic[letter] = abs(i - dis_dic.get(letter, 0))

        for i in range(len(distance)):
            letter = chr(i + 97)
            if dis_dic.get(letter, 0) != 0 and distance[i] != dis_dic.get(letter, 0) - 1:
                return False
        return True
