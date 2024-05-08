"""
506. Relative Ranks
https://leetcode.com/problems/relative-ranks
"""


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {v: i for i, v in enumerate(sorted(score, reverse=True))}
        output = []
        for i in range(len(score)):
            rank = (dic[score[i]])
            if rank == 0:
                output.append('Gold Medal')
            elif rank == 1:
                output.append('Silver Medal')
            elif rank == 2:
                output.append('Bronze Medal')
            else:
                output.append(str(rank + 1))
        return output
