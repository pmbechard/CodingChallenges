"""
950. Reveal Cards In Increasing Order
https://leetcode.com/problems/reveal-cards-in-increasing-order
"""


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        new_deck = [deck.pop()]
        while deck:
            new_deck.insert(0, new_deck.pop())
            new_deck.insert(0, deck.pop())
        return new_deck
