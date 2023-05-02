"""
2660. Determine the Winner of a Bowling Game
https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
"""


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1_score = self.get_score(player1)
        p2_score = self.get_score(player2)
        if p1_score > p2_score:
            return 1
        elif p1_score < p2_score:
            return 2
        else:
            return 0

    def get_score(self, turns: List[int]) -> int:
        score = bonus = 0
        for i in range(len(turns)):
            if bonus > 0:
                score += turns[i]
                bonus -= 1
            if turns[i] == 10:
                bonus = 2
            score += turns[i]
        return score
