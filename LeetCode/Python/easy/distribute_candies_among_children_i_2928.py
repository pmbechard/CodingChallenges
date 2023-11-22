"""
2928. Distribute Candies Among Children I
https://leetcode.com/problems/distribute-candies-among-children-i/
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        counted = set()
        for i in range(limit + 1):
            for j in range(i, limit + 1):
                k = n - i - j
                if k > limit or k < max(i, j) or (i, j, k) in counted:
                    continue
                counted.add((i, j, k))
                x = len(set([i, j, k]))
                count += (x * (x + 1)) // 2
        return count
