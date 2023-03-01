"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] = anagrams.get(sorted_s, []) + [s]
        return anagrams.values()
