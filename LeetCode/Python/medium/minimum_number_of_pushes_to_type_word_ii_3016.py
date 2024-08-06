"""
3016. Minimum Number of Pushes to Type Word II
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
"""


class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = uniq = 0
        ctr = Counter(word)
        while ctr:
            most = ctr.most_common(1)[0]
            pushes += most[1] * ((uniq // 8) + 1)
            del ctr[most[0]]
            uniq += 1
        return pushes
