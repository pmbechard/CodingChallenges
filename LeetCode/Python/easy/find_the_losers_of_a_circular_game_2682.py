"""
2682. Find the Losers of the Circular Game
https://leetcode.com/problems/find-the-losers-of-the-circular-game/
"""


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        dic = {i: 0 for i in range(1, n + 1)}
        pos = counter = dic[1] = 1
        while True:
            pos = pos + counter * k
            while pos > n: pos -= n
            if dic[pos] == 1:
                break
            else:
                dic[pos] += 1
            counter += 1
        return sorted([k for k, v in dic.items() if v == 0])
