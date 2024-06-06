"""
846. Hand of Straights
https://leetcode.com/problems/hand-of-straights/
"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        while hand:
            if not self.remove_seq(hand, groupSize):
                return False
        return True

    def remove_seq(self, hand, groupSize):
        for card in range(hand[0], hand[0] + groupSize):
            try:
                hand.remove(card)
            except ValueError:
                return False
        return True
