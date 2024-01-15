"""
2225. Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = dict([(k, 0) for k in set(chain.from_iterable(matches))])
        for match in matches:
            players[match[1]] += 1
        result = [[], []]
        for k, v in players.items():
            if v == 0:
                result[0].append(k)
            elif v == 1:
                result[1].append(k)
        result[0].sort()
        result[1].sort()
        return result
