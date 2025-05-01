"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tab = [None] * (target + 1)
        tab[0] = [[]]

        for i in range(target + 1):
            if tab[i] == None: continue
            for num in candidates:
                if num + i < target + 1:
                    for comb in tab[i]:
                        if not comb or num >= comb[0]:
                            if tab[i + num] == None:
                                tab[i + num] = [];
                            tab[i + num].append([num] + comb)
        return tab[-1] or []
