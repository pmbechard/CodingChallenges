"""
846. Hand of Straights
https://leetcode.com/problems/hand-of-straights/
"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        ctr = Counter(hand)
        while ctr:
            if not self.get_straight(ctr, groupSize):
                return False
        return True

    def get_straight(self, ctr, groupSize):
        a = min(ctr)
        for _ in range(groupSize):
            if not ctr[a]:
                return False
            ctr[a] -= 1
            if ctr[a] == 0:
                del ctr[a]
            a += 1
        return True
