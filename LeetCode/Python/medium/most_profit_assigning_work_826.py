"""
826. Most Profit Assigning Work
https://leetcode.com/problems/most-profit-assigning-work/
"""


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        total = 0
        worker.sort(reverse=True)
        for d, p in sorted(zip(difficulty, profit), key=lambda x: -x[1]):
            i = 0
            while i < len(worker) and d <= worker[i]:
                i += 1
            total += i * p
            worker = worker[i:]
            if not worker: break
        return total
