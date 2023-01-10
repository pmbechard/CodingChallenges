"""
821. Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        results = []
        for i in range(len(s)):
            prev_c = s[:i][::-1].find(c)
            next_c = s[i:].find(c)
            if prev_c < 0:
                results.append(next_c)
            elif next_c < 0:
                results.append(prev_c + 1)
            else:
                results.append(min(prev_c + 1, next_c))
        return results
