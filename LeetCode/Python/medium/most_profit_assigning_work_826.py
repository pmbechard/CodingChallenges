"""
826. Most Profit Assigning Work
https://leetcode.com/problems/most-profit-assigning-work/
"""


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_prof = sorted(zip(difficulty, profit), key=lambda x: -x[1])
        cntr = Counter(worker)
        total = i = 0
        for w in sorted(cntr, reverse=True):
            while i < len(diff_prof) and w < diff_prof[i][0]:
                i += 1
            if i < len(diff_prof):
                total += diff_prof[i][1] * cntr[w]
        return total
