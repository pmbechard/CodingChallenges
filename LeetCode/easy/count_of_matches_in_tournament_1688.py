"""
1688. Count of Matches in Tournament
https://leetcode.com/problems/count-of-matches-in-tournament/
"""


class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n != 1:
            if n % 2 == 0:
                total += n//2
                n = n//2
            else:
                total += (n-1)//2
                n = (n-1)//2+1
        return total
