"""
2347. Best Poker Hand
https://leetcode.com/problems/best-poker-hand/
"""


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1: return 'Flush'
        count = 0
        for rank in ranks:
            rank_count = ranks.count(rank)
            if rank_count > count:
                count = rank_count
        if count >= 3:
            return "Three of a Kind"
        elif count == 2:
            return "Pair"
        else:
            return "High Card"
